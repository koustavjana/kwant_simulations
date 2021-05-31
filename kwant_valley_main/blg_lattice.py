import kwant
from math import pi,sqrt,tanh
import numpy as np
from matplotlib import pyplot
from kwant.digest import uniform
from types import SimpleNamespace

sin_30, cos_30 = (1 / 2, sqrt(3) / 2)
graphene = kwant.lattice.general([(1, 0), (sin_30, cos_30)],
								 [(0, 0), (0, 1 / sqrt(3)), (0, 1 / sqrt(3)), (0, 2 / sqrt(3))])
aL,bL,aU,bU = graphene.sublattices

# def lin0(y,W,jw) :
# 	if y < -jw :
# 		return -1 
# 	elif -jw <= y < jw :
# 		return y/jw
# 	else :
# 		return 1

def lin0(y,W,jw) :
	return tanh((y)/(jw/2))


def make_system(W = 10*sqrt(3), L = 10, delta = 0, t = 1.6, tl = 0.8) :
	def channel(pos):
		x, y = pos
		return (0 <= x <= L) and (-W/2 < y <= W/2)    

	syst = kwant.Builder()
	
	del_fn = lambda y,W : lin0(y,W,W/20) 
	
	def potential(site, U, U_disorder):
		(x, y) = site.pos
		salt = 0
		d = -1
		if (site.family == bU) or (site.family == aU) :
			d = 1
		term1 = d*delta*del_fn(y,W)
		term2 = U
		term3 = U_disorder * (uniform(repr(site), repr(salt)) - 0.5)
		return term1 + term2 + term3

	def dummy(site):
		(x, y) = site.pos
		d = -1
		if (site.family == bU) or (site.family == aU) :
			d = 1
		term1 = d*delta*del_fn(y,W)
		return term1 

	syst[graphene.shape(channel, (0, 0))] = potential
	hoppings = (((0, 0), aL, bL), ((0, 1), aL, bL), ((-1, 1), aL, bL), ((0, 0), aU, bU), ((0, 1), aU, bU), ((-1, 1), aU, bU))
	syst[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t
	kind = kwant.builder.HoppingKind((0, 0), aU, bL)
	syst[kind(syst)] = -tl

	# left lead
	sym0 = kwant.TranslationalSymmetry(graphene.vec((-1, 0)))

	def lead0_shape(pos):
		x, y = pos
		return (-W/2 < y <= W/2)

	lead0 = kwant.Builder(sym0)
	lead0[graphene.shape(lead0_shape, (0, 0))] = 0
	lead0[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t
	lead0[kind(lead0)] = -tl

	# right lead
	sym1 = kwant.TranslationalSymmetry(graphene.vec((1, 0)))

	def lead1_shape(pos):
		x, y = pos
		return (-W/2 < y <= W/2)

	lead1 = kwant.Builder(sym1)
	lead1[graphene.shape(lead1_shape, (0, 0))] = 0
	lead1[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t
	lead1[kind(lead1)] = -tl

	# dummy lead for bandstructure
	sym_dum = kwant.TranslationalSymmetry(graphene.vec((1, 0)))

	def dum_lead_shape(pos):
		x, y = pos
		return (-W/2 < y <= W/2)

	dum_lead = kwant.Builder(sym_dum)
	dum_lead[graphene.shape(dum_lead_shape, (0, 0))] = dummy
	dum_lead[[kwant.builder.HoppingKind(*hopping) for hopping in hoppings]] = -t
	dum_lead[kind(dum_lead)] = -tl

	return syst, [lead0, lead1], dum_lead



