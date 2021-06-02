clear;
clc;
close all;

M2 = csvread('valley_blg_d20_l20_disorder_6.csv');
M4 = csvread('valley_blg_d20_l40_disorder_6.csv');
M6 = csvread('valley_blg_d20_l80_disorder_6.csv');

figure
plot(M2(:,1),100*(M2(:,3)-M2(:,2))./(M2(:,2)+M2(:,3)),'Linewidth',2.5)
hold on;
plot(M4(:,1),100*(M4(:,3)-M4(:,2))./(M4(:,2)+M4(:,3)),'Linewidth',2.5)
hold on;
plot(M6(:,1),100*(M6(:,3)-M6(:,2))./(M6(:,2)+M6(:,3)),'Linewidth',2.5)
hold off
set(gca,'linewidth',2,'fontname','Helvetica','fontsize',20)
set(gca,'ticklength',[0.025 0.025])
xlim([-0.3 0.3])
% ylim([0 100])
xlabel('E_{F}-U in eV')
ylabel('Valley Polarization(%)')
title('Varied Channel Length')
legend('5nm','10nm','20nm','Location','best')
grid on
saveas(gcf,'valley_blg_d20_l_disorder_6.jpg')