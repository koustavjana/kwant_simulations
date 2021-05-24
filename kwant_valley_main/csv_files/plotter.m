clear;
clc;
close all;

M0 = csvread('valley_silicene1_disorder_0.csv');
M2 = csvread('valley_silicene1_disorder_2.csv');
M4 = csvread('valley_silicene1_disorder_4.csv');
M6 = csvread('valley_silicene1_disorder_6.csv');

figure
plot(M0(:,1),(M0(:,3)-M0(:,2))./(M0(:,2)+M0(:,3)),'Linewidth',2.5)
hold on;
plot(M2(:,1),(M2(:,3)-M2(:,2))./(M2(:,2)+M2(:,3)),'Linewidth',2.5)
hold on;
plot(M4(:,1),(M4(:,3)-M4(:,2))./(M4(:,2)+M4(:,3)),'Linewidth',2.5)
hold on;
plot(M6(:,1),(M6(:,3)-M6(:,2))./(M6(:,2)+M6(:,3)),'Linewidth',2.5)
hold off
set(gca,'linewidth',2,'fontname','Helvetica','fontsize',20)
set(gca,'ticklength',[0.025 0.025])
% xlim()
ylim([0 1])
xlabel('E_{F}-U in eV')
ylabel('Valley Polarization')
title('Varied Disorder Strength')
legend('0','2\Delta','4\Delta','6\Delta','Location','best')
grid on