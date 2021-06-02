clear;
clc;
close all;

M = csvread('silicene_band_d20_rev.csv');

figure
plot(M(:,1)./pi,M(:,2:end),'LineWidth',2)
set(gca,'linewidth',2,'fontname','Helvetica','fontsize',20)
set(gca,'ticklength',[0.025 0.025])
ylim([-1.6 1.6])
xlabel('k_{x}a(units of \pi)')
ylabel('E in eV')
title('Silicene band structure')
grid on
% saveas(gcf,'silicene_band_d20_rev.jpg')