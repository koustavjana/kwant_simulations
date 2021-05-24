clear;
clc;
close all;

M = csvread('silicene1_band.csv');

figure
plot(M(:,1),M(:,2:321),'LineWidth',2)
set(gca,'linewidth',2,'fontname','Helvetica','fontsize',20)
set(gca,'ticklength',[0.025 0.025])
ylim([-1.6 1.6])
xlabel('k_{x}a')
ylabel('E in eV')
title('Silicene band structure')
grid on