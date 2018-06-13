

M = 100;
N = 4;
x = linspace(-20, 20, M)';
X = [ones(M,1), x, x.^2, x.^3, x.^4];
X
% or 
% X = zeros(M, N + 1)
% for i = 0:1:N
%     for j = 1:M
%         X(j, i + 1) = x(j).^i;
%     end
% end
% X

clc; 
close all;
noise = 20 * randn([1, M])';
beta = [12, -12, 2, 0.1, 0.1]';

y = X * beta + noise;  % y size is 
plot(x, y, '*')

X = X(:,1:5);
beta_r = X'*X\(X'*y);
y_r = X * beta_r;
hold on
plot(x, y_r, 'r')
title(beta_r)
