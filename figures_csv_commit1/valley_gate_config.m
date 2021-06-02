clear;
clc;
close all;

M = csvread('valley_silicene_d20_l40_disorder_0.csv');
Mrev = csvread('valley_silicene_d20_l40_disorder_0_rev.csv');

figure
% plot(M(:,1),100*(M(:,3)-M(:,2))./(M(:,2)+M(:,3)),'Linewidth',2.5)
hold on;
plot(Mrev(:,1),100*(Mrev(:,3)-Mrev(:,2))./(Mrev(:,2)+Mrev(:,3)),'Linewidth',2.5)
hold off
set(gca,'linewidth',2,'fontname','Helvetica','fontsize',20)
set(gca,'ticklength',[0.025 0.025])
xlim([-0.3 0.3])
% ylim([0 100])
xlabel('E_{F}-U in eV')
ylabel('Valley Polarization(%)')
title('Negative Polarization')
grid on
saveas(gcf,'valley_silicene_d20_l40_negative.jpg')