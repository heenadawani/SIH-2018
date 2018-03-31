function y = automationgg(a)
i = imread(a);
i=~i;
[w,h] = size(i);
sectionx = w*0.1;
sectiony = h*0.5;
sectionheight = h*0.4;
sectionwidth = w*0.8;
section = imcrop(i,[sectionx sectiony sectionwidth sectionheight]);


[h1,w1] = size(section);
cropleft = imcrop(section,[0 0 w1*0.5 h1]);
cropright = imcrop(section,[w1*0.5 0 w1*0.5 h1]);
%cropleft = imbinarize(cropleft);
%cropright = imbinarize(cropright);

largeleft = bwareafilt(cropleft,1);
largeright = bwareafilt(cropright,1);
lr = regionprops(largeleft,'BoundingBox');
rr = regionprops(largeright,'BoundingBox');
lrwh = size(cropleft,2) - lr.BoundingBox(1);
rrwh = rr.BoundingBox(3)+ rr.BoundingBox(1);

heartleft = ~largeleft;
heartright = ~largeright;

if(lrwh <= size(largeleft,2)) && (lrwh > size(largeleft,2)*0.97) 
    xlargeleft = size(largeleft,2)*0.03;
    widthlargeleft = size(largeleft,2)*0.97;
    largeleft1 = imcrop(largeleft,[xlargeleft 0 widthlargeleft h1]);
    largeleft2 = bwareafilt(largeleft1,1);
    lr = regionprops(largeleft2,'BoundingBox');
    lrwh = size(largeleft1,2) - lr.BoundingBox(1);
    heartleft = ~largeleft2;
end

if(rrwh <= size(largeright,2)) && (rrwh > size(largeright,2)*0.97) 
    
    widthlargeright = size(largeright,2)*0.97;
    largeright1 = imcrop(largeright,[0 0 widthlargeright h1]);
    largeright2 = bwareafilt(largeright1,1);
    rr = regionprops(largeright2,'BoundingBox');
    rrwh = rr.BoundingBox(3)+ rr.BoundingBox(1);
    heartright = ~largeright2;
    
end

lungwidth = lrwh + rrwh;
heartleft = ~heartleft;
heartright = ~heartright;
heartlefttemp = regionprops(heartleft,'BoundingBox');
heartrighttemp = regionprops(heartright,'BoundingBox');
heartlefttempwidth = size(heartleft,2) - heartlefttemp.BoundingBox(1);
heartleft = imcrop(heartleft,[heartlefttemp.BoundingBox(1) 0 heartlefttempwidth heartlefttemp.BoundingBox(4)]);
heartrighttempwidth = heartrighttemp.BoundingBox(1) + heartrighttemp.BoundingBox(3);
heartright = imcrop(heartright,[0 0 heartrighttempwidth heartrighttemp.BoundingBox(4)]);

heartleft = ~heartleft;
heartright = ~heartright;
heartleft = bwareafilt(heartleft,1);
heartright = bwareafilt(heartright,1);

leftheartregion = regionprops(heartleft,'BoundingBox');
rightheartregion = regionprops(heartright,'BoundingBox');

lefthw =  size(heartleft,2)- leftheartregion.BoundingBox(1);
righthw = rightheartregion.BoundingBox(3);

leftw1width = size(heartleft,2);
leftw1height = size(heartleft,1)*0.75;
lefthw1 = imcrop(heartleft,[0 0 leftw1width leftw1height]);
rightw1height = size(heartright,1)*0.75;
righthw1 = imcrop(heartright,[0 0 leftw1width rightw1height]);

lefthw1only = bwareafilt(lefthw1,1);
righthw1only = bwareafilt(righthw1,1);
lefthw1onlybb1 = regionprops(lefthw1only,'BoundingBox');
righthw1onlybb1 = regionprops(righthw1only,'BoundingBox');

lefthwext1 = size(heartleft,2) - lefthw1onlybb1.BoundingBox(1);
righthwext1 = righthw1onlybb1.BoundingBox(3);

leftw2height = size(heartleft,1)*0.5;
lefthw2 = imcrop(lefthw1,[0 0 leftw1width leftw2height]);
rightw2height = size(heartright,1)*0.5;
righthw2 = imcrop(righthw1,[0 0 leftw1width rightw2height]);

lefthw2only = bwareafilt(lefthw2,1);
righthw2only = bwareafilt(righthw2,1);
lefthw1onlybb2 = regionprops(lefthw2only,'BoundingBox');
righthw1onlybb2 = regionprops(righthw2only,'BoundingBox');

lefthwext2 = size(heartleft,2) - lefthw1onlybb2.BoundingBox(1);
righthwext2 = righthw1onlybb2.BoundingBox(3);

leftw3height = size(heartleft,1)*0.25;
lefthw3 = imcrop(lefthw2,[0 0 leftw1width leftw3height]);
rightw3height = size(heartright,1)*0.25;
righthw3 = imcrop(righthw2,[0 0 leftw1width rightw3height]);

lefthw3only = bwareafilt(lefthw3,1);
righthw3only = bwareafilt(righthw3,1);
lefthw1onlybb3 = regionprops(lefthw3only,'BoundingBox');
righthw1onlybb3 = regionprops(righthw3only,'BoundingBox');

lefthwext3 = size(heartleft,2) - lefthw1onlybb3.BoundingBox(1);
righthwext3 = righthw1onlybb3.BoundingBox(3);



if(lefthw>=lefthwext1) && (lefthw>=lefthwext2) && (lefthw>=lefthwext3)
    if(lefthwext3>=lefthwext2)
        considerleft= lefthwext3;
       
    else
        considerleft=lefthwext2;
    end
elseif(lefthw<lefthwext1) || (lefthw<lefthwext2) || (lefthw<lefthwext3)
    if(lefthwext2>lefthwext1)
        considerleft = lefthwext2;
    else
        considerleft = lefthwext1;
    end
end

if(righthw>=righthwext1) && (righthw>=righthwext2) && (righthw>=righthwext3)
    if(righthwext3>=righthwext2)
        considerright= righthwext3;
       
    else
        considerright=righthwext2;
    end
elseif(righthw<righthwext1) || (righthw<righthwext2) || (righthw<righthwext3)
    if(rightwext2>righthwext1)
        considerright = righthwext2;
    else
        considerright = righthwext1;
    end
end
heartwidth = considerleft+considerright;

ctr = heartwidth/lungwidth;


sectionx1 = w*0.1;
sectiony1 = h*0.2;
sectionheight1 = h*0.3;
sectionwidth1 = w*0.8;
section1 = imcrop(i,[sectionx1 sectiony1 sectionwidth1 sectionheight1]);


[h11,w11] = size(section1);
cropleft1 = imcrop(section1,[0 0 w11*0.5 h11]);
cropright1 = imcrop(section1,[w11*0.5 0 w11*0.5 h11]);
%cropleft1 = imbinarize(cropleft1);
%cropright1 = imbinarize(cropright1);

largeleft1 = bwareafilt(cropleft1,1);
largeright1 = bwareafilt(cropright1,1);

lr1 = regionprops(largeleft1,'BoundingBox');
rr1 = regionprops(largeright1,'BoundingBox');
lrwh1 = size(cropleft1,2) - lr1.BoundingBox(1);
rrwh1 = rr1.BoundingBox(3)+ rr1.BoundingBox(1);

heartleft1 = ~largeleft1;
heartright1 = ~largeright1;

if(lrwh1 <= size(largeleft1,2)) && (lrwh1 > size(largeleft1,2)*0.95) 
    xlargeleft1 = size(largeleft1,2)*0.15;
    widthlargeleft1 = size(largeleft1,2)*0.85;
    largeleft11 = imcrop(largeleft1,[xlargeleft1 0 widthlargeleft1 h11]);
    largeleft21 = bwareafilt(largeleft11,1);
    lr1 = regionprops(largeleft21,'BoundingBox');
    lrwh1 = size(largeleft11,2) - lr1.BoundingBox(1);
    heartleft1 = ~largeleft21;
end

if(rrwh1 <= size(largeright1,2)) && (rrwh1 > size(largeright1,2)*0.95) 
    
    widthlargeright1 = size(largeright1,2)*0.85;
    largeright11 = imcrop(largeright1,[0 0 widthlargeright1 h11]);
    largeright21 = bwareafilt(largeright11,1);
    rr1 = regionprops(largeright21,'BoundingBox');
    rrwh1 = rr1.BoundingBox(3)+ rr1.BoundingBox(1);
    heartright1 = ~largeright21;
    
end

lungwidth1 = lrwh1 + rrwh1;

heartleft1 = ~heartleft1;
heartright1 = ~heartright1;
heartlefttemp1 = regionprops(heartleft1,'BoundingBox');
heartrighttemp1 = regionprops(heartright1,'BoundingBox');
heartlefttempwidth1 = size(heartleft1,2) - heartlefttemp1.BoundingBox(1);
heartleft1 = imcrop(heartleft1,[heartlefttemp1.BoundingBox(1) heartlefttemp1.BoundingBox(2) heartlefttempwidth1 heartlefttemp1.BoundingBox(4)]);
heartrighttempwidth1 = heartrighttemp1.BoundingBox(1) + heartrighttemp1.BoundingBox(3);
heartright1 = imcrop(heartright1,[0 heartrighttemp1.BoundingBox(2) heartrighttempwidth1 heartrighttemp1.BoundingBox(4)]);
    
heartleft1 = ~heartleft1;
heartright1 = ~heartright1;
heartleft1 = bwareafilt(heartleft1,1);
heartright1 = bwareafilt(heartright1,1);

leftheartregion1 = regionprops(heartleft1,'BoundingBox');
rightheartregion1 = regionprops(heartright1,'BoundingBox');


lefthw1 =  size(heartleft1,2)- leftheartregion1.BoundingBox(1);
righthw1 = rightheartregion1.BoundingBox(3);

leftw1width1 = size(heartleft1,2);
leftw1height1 = size(heartleft1,1)*0.75;
lefthw11 = imcrop(heartleft1,[0 0 leftw1width1 leftw1height1]);
rightw1height1 = size(heartright1,1)*0.75;
righthw11 = imcrop(heartright1,[0 0 leftw1width1 rightw1height1]);

lefthw1only1 = bwareafilt(lefthw11,1);
righthw1only1 = bwareafilt(righthw11,1);
lefthw1onlybb11 = regionprops(lefthw1only1,'BoundingBox');
righthw1onlybb11 = regionprops(righthw1only1,'BoundingBox');

lefthwext11 = size(heartleft1,2) - lefthw1onlybb11.BoundingBox(1);
righthwext11 = righthw1onlybb11.BoundingBox(3);

if(lefthw1>=lefthwext11) 
    considerleft1 = lefthw1;
else
    considerleft1 = lefthwex11;
end

if(righthw1>=righthwext11) 
    considerright1 = righthw1;
else
    considerright1 = righthwex11;
end


heartwidth1 = considerleft1+considerright1;

ctr1 = heartwidth1/lungwidth1;


if(ctr<0.25) || (ctr>0.75)
    ctrfinal = ctr1;
else
    ctrfinal = ctr;
end

y = ctrfinal;
end