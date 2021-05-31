import kwant
from math import pi,sqrt,tanh
import numpy as np
from matplotlib import pyplot
from kwant.digest import uniform
from types import SimpleNamespace

sin_30, cos_30 = (1 / 2, sqrt(3) / 2)
graphene = kwant.lattice.general([(1, 0), (sin_30, cos_30)],
								 [(0, 0), (0, 1 / sqrt(3))])

a, b = graphene.sublattices

def lin0(y,W,jw) :
	return tanh((y)/(jw/2))

def make_system(W = 10*sqrt(3), L = 10, delta = 0, t = 1.6) :

	def channel(pos):
		x, y = pos
		return (0 <= x <= L) and (-W/2 < y <= W/2)    

	syst = kwant.Builder()
	
	del_fn = lambda y,W : lin0(y,W,W/20)  	
	
	def potential(site, U, U_disorder):
		(x, y) = site.pos
		salt = 0
		d = -1
		if (site.family == a) :
			d = 1
		term1 = d*delta*del_fn(y,W)
		term2 = U
		term3 = U_disorder * (uniform(repr(site), repr(salt)) - 0.5)
		return term1 + term2 + term3


	def dummy(site):
		(x, y) = site.pos
		d = -1
		if (site.family == a) :
			d = 1
		term1 = d*delta*del_fn(y,W)
		return term1


	syst[graphene.shape(channel, (0, 0))] = potential
	hoppings = (((0, 0), a, b), ((0, 1), a, b), ((-1, 1), a, b))
	syst[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t

	# left lead
	sym0 = kwant.TranslationalSymmetry(graphene.vec((-1, 0)))

	def lead0_shape(pos):
		x, y = pos
		return (-W/2 < y <= W/2)

	lead0 = kwant.Builder(sym0)
	lead0[graphene.shape(lead0_shape, (0, 0))] = 0
	lead0[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t	

	# right lead
	sym1 = kwant.TranslationalSymmetry(graphene.vec((1, 0)))

	def lead1_shape(pos):
		x, y = pos
		return (-W/2 < y <= W/2)

	lead1 = kwant.Builder(sym1)
	lead1[graphene.shape(lead1_shape, (0, 0))] = 0
	lead1[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t


	# dummy lead
	dum_sym = kwant.TranslationalSymmetry(graphene.vec((1, 0)))

	def dum_lead_shape(pos):
		x, y = pos
		return (-W/2 < y <= W/2)

	dum_lead = kwant.Builder(dum_sym)
	dum_lead[graphene.shape(dum_lead_shape, (0, 0))] = dummy
	dum_lead[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t

	return syst, [lead0, lead1], dum_lead




