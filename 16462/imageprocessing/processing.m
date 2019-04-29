%a='F:\testing_ip'
function processing(a,b,n)
myFolder = a; %source image
if ~isdir(myFolder)
  %errorMessage = sprintf('Error: The following folder does not exist:\n%s', myFolder);%op 1
  uiwait(warndlg(errorMessage));
  return;
end
filePattern = fullfile(myFolder, '*.PNG');
jpegFiles = dir(filePattern);
for k = 1:n%length(jpegFiles)
  baseFileName = jpegFiles(k).name;
  fullFileName = fullfile(myFolder, baseFileName);
  fprintf(1, 'Now reading %s\n', fullFileName);
  i= imread(fullFileName);
  l= histeq(i);  %for enhacing the image
J = imnoise(l,'gaussian');
K= imgaussfilt(J,0.5);   %for filtering the image, standard deviation is by default is 0.5 in gaussian filter 
level = graythresh(K);   %segmentationk using otsu algo
BW = im2bw(K,level);     %binary images 
%imshow(BW);  % Display image.
  %imwrite(imageArray);
  %imwrite(imageArray,fullfile('ResizedAx',H));
%baseFileName = sprintf('%d.png', k); % 
fullFileName = fullfile(b, baseFileName); %destination image 
imwrite(BW, fullFileName);
% Force display to update immediately.
drawnow;
end
end
