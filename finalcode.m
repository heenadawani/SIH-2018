clc;
clear all;
close all;
i=imread('E:\Downloads\images\images\00000373_000.png');
K = imadjust(i,[0.4 0.6],[]);
%T=adaptthresh(i,0.700);
%Ibw=imbinarize(i,T);
%figure
%imshowpair(i,Ibw,'montage')
threshold =128;
Ibw = K>threshold;  
subplot(1,2,1)
subimage(i);title('input image');
subplot(1,2,2)
subimage(Ibw);title('output image');
%d=imdistline);

%%
[x1,y1] = ginput(1);
[x2,y2] = ginput(1);
line([x1,x2],[y1,y1],'LineWidth',3);
distlung  = sqrt((x2-x1)^2 + (y1-y1)^2);

[x3,y3] = ginput(1);
[x4,y4] = ginput(1);
line([x3,x4],[y3,y3],'color','r','LineWidth',3);
distheart  = sqrt((x4-x3)^2 + (y3-y3)^2);

ctr=distheart/distlung;

if ctr > 1
    ctr=1/ctr;
end

if ctr < 0.50
    fprintf('No Cardiomegaly');
else
    fprintf('Cardiomegaly');
end

ctr