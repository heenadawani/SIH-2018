clc;
clear all;
close all;

i= imread('00000096_000.png18.png');
figure,imshow(i);
%%
%figure,imhist(i);
%K = imadjust(i,[0.4 0.6],[]);  
l= histeq(i);      %for enhacing the image
figure,imshow(l);
%%
K= imgaussfilt(l,0.5);   %for filtering the image, standard deviation is by default is 0.5 in gaussian filter 
figure,imshow(K);
%%
level = graythresh(K);   %segmentationk using otsu algo
BW = im2bw(K,level);     %binary images 
%threshold =128;
%Ibw = K>threshold; 
figure,imshow(BW);
%%
subplot(1,2,1)
subimage(i);title('Input Image');

subplot(1,2,2)
subimage(BW);title('Output Image');

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
disp(ctr);
if ctr > 1
   ctr=1/ctr;
end

if ctr < 0.50
   fprintf('No Cardiomegaly');
else
   fprintf('Cardiomegaly');
end
