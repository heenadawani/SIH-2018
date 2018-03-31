clc;
clear all;
close all;

i= imread('0.png');
figure,imshow(i);
%%
%figure,imhist(i);
  
l= histeq(i);      %for enhancing the image(enhancement)
figure,imshow(l);
%%

K= imgaussfilt(l,0.5);   %for filtering the image,digitized image (filtering) standard deviation is by default is 0.5 in gaussian filter 
figure,imshow(K);
%%
level = graythresh(K);   %(thresholding) using otsu algo
BW = im2bw(K,level);     %binary images 
figure,imshow(BW);
%%
subplot(1,2,1)
subimage(i);title('Input Image');

subplot(1,2,2)
subimage(BW);title('Output Image');

