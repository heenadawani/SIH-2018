clc;
close all;
clear all;
ref=imread('reference.png');
reference=im2uint16(ref);
%imshow(i);
i = imread('00010225_000.png');
%[ssimval, ssimmap] = ssim(i,reference);
%imshow(ssimmap);[ssimval, ssimmap] = ssim(imidx==i,ref);
%%
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
imidxcopy = reshape(idx, size(i));
%%
%[width,height,color] = size(imidxcopy==1);
%heightnew = height*0.8;
%widthnew = width*0.8;
%xcoord = width*0.1;
%ycoord = height*0.1;
%r = imrect(gca,[xcoord ycoord widthnew heightnew]);
%for j=1:8
%    h_im = imshow(imidxcopy==1);
%    BW = createMask(r,h_im);
%    ROI = (imidxcopy==1);
%    ROI(BW == 0) = 0;
%end    
%figure, imshow(ROI);


%%
%figure,
    subplot(2,4,1),imshow(imidx==1);
    subplot(2,4,2),imshow(imidx==2);
    subplot(2,4,3),imshow(imidx==3);
    subplot(2,4,4),imshow(imidx==4);
    subplot(2,4,5),imshow(imidx==5);
    subplot(2,4,6),imshow(imidx==6);
    subplot(2,4,7),imshow(imidx==7);
    subplot(2,4,8),imshow(imidx==8);
    %%
    v=[0 0 0 0 0 0 0 0];
    f=0;
    s=0;
    t=0;
    fi=0;
    si=0;
    ti=0;
    for i = 1:8        
        ssimval = immse(im2uint16(imidx==i),reference);
        disp(ssimval)
        if(ssimval>f)
            t=s;
            ti=si
            s=f;
            si=fi
            f=ssimval;
            fi=i
        elseif(ssimval>s)
            t=s;
            ti=si;
            s=ssimval;
            si=i;
        elseif(ssimval>t)
            t=ssimval;
            ti=i;
        end
        
        
        v(i)=ssimval;
    end
    disp(f)
    disp(s)
    disp(t)   
    disp(fi)
    disp(si)
    disp(ti)       
%%
frame1 = (imidx == fi);
frame2 = (imidx == si);
%frame3 = (imidx == ti);
%frame4=(imidx==1);
bw = frame1 | frame2 ;
%bw = bwareafilt(bw,2);
figure,imshow(bw);
bw=~bw;
lungsonly = bwareafilt(bw,2);
imshow(lungsonly)
