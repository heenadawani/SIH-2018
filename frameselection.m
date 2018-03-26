clc;
close all;
clear all;
%i = imread('00000033_000.png');
i = imread(fullFileName);
% Get the dimensions of the image.  
% numberOfColorBands should be = 1.
[rows, columns, numberOfColorChannels] = size(i);
if numberOfColorChannels > 1
	% It's not really gray scale like we expected - it's color.
	% Convert it to gray scale by taking only the green channel.
    i = rgb2gray(i);	 % Take green channel.
end
%%

p=reshape(i,[],1);
p=double(p);
%p = entropyfilt(p);
[idx, nn] = kmeans(p,8);
imidx=reshape(idx,size(i));
figure,
    subplot(2,4,1),imshow(imidx==1);
    subplot(2,4,2),imshow(imidx==2);
    subplot(2,4,3),imshow(imidx==3);
    subplot(2,4,4),imshow(imidx==4);
    subplot(2,4,5),imshow(imidx==5);
    subplot(2,4,6),imshow(imidx==6);
    subplot(2,4,7),imshow(imidx==7);
    subplot(2,4,8),imshow(imidx==8);
%%
frame1 = (imidx == 6);
frame2 = (imidx == 4);
frame3 = (imidx == 8);
%frame4=(imidx==1);
bw = frame1 | frame2 | frame3;
%bw=bw&frame4;
%figure, imshow(bw);
lungsonly = bwareafilt(bw,2);
figure, imshow(lungsonly);
%%
s = regionprops(lungsonly,'BoundingBox');
lungwidth = s(2).BoundingBox(3) + sqrt((s(1).BoundingBox(1) - s(2).BoundingBox(1))^2);
lungheight = max(s(1).BoundingBox(4),s(2).BoundingBox(4));
lungx = min(s(1).BoundingBox(1),s(2).BoundingBox(1));
lungy = min(s(1).BoundingBox(2),s(2).BoundingBox(2));
out = imcrop(lungsonly,[lungx lungy lungwidth lungheight]);
figure, imshow(out);
hearty = lungheight/2;
heartheight = lungheight*0.40;
heart = imcrop(out,[0 hearty lungwidth heartheight]);
heart = bwareafilt(~heart,1);
%figure, imshow(heart);
%%
s1 = regionprops(heart,'BoundingBox');
heartwidth1 = s1.BoundingBox(3);
heartheight1 = lungheight*0.3;
temp = imcrop(heart,[0 0 lungwidth heartheight1]);

temp = bwareafilt(temp,1);
s2 = regionprops(temp,'BoundingBox');
heartwidth2 = s2.BoundingBox(3);
heartheight2 = lungheight*0.2;
temp2 = imcrop(temp,[0 0 lungwidth heartheight2]);

temp2 = bwareafilt(temp2,1);
s3 = regionprops(temp2,'BoundingBox');
heartwidth3 = s3.BoundingBox(3);
%heartheight3 = lungheight*0.1;
%temp3 = imcrop(temp2,[0 0 lungwidth heartheight3]);
%figure, imshow(temp3);
%%
if(heartwidth2<heartwidth1)
    if(heartwidth3>heartwidth2)
        realheartwidth = heartwidth3;
    elseif(heartwidth3<heartwidth2)
        realheartwidth = heartwidth2;
    end
else
    realheartwidth = heartwidth1;
end
%%
ctr = realheartwidth/lungwidth;

if ctr < 0.50
   fprintf('No Cardiomegaly');
   fprintf('\n');
   fprintf('CTR is: ');
   disp(ctr)
else
   fprintf('Cardiomegaly');
   fprintf('\n');
   fprintf('CTR is: ');
   disp(ctr)
end