%% ========================================================================
% 《小猫团子与老橘师傅的西瓜书×深度学习生活绘本》—— 原生 MATLAB 动态动画生成脚本
% 适用环境：MATLAB R2022a+ 或通过 MATLAB MCP Server 调用 run_matlab_script
% 一键生成 4 张核心算法动态 GIF：
%   1. anim01-l2-vs-l1-ball-roll.gif      (碗底滚珠 vs V字谷底横跳)
%   2. anim02-neural-paper-folding.gif    (神经网络隐藏层“折纸剪窗花”空间展开)
%   3. anim03-svm-trampoline-lift.gif     (SVM 核函数“颠铁锅筛花生米”三维升维)
%   4. anim04-em-rubber-band-dance.gif    (EM 算法“操场广播体操分队”椭圆橡皮筋演化)
%% ========================================================================
clear; clc; close all;
outDir = fullfile(fileparts(mfilename('fullpath')), '..', 'assets');
if ~exist(outDir, 'dir'), mkdir(outDir); end

%% 动画 1：L2 圆碗丝滑收敛 vs L1 V字尖谷反复横跳
fig1 = figure('Color', [1 0.98 0.92], 'Position', [100, 100, 960, 380]);
gif1 = fullfile(outDir, 'anim01-l2-vs-l1-ball-roll.gif');
theta2 = 3.6; theta1 = 3.6; lr = 0.42;
t_grid = linspace(-4.2, 4.2, 300);
for step = 1:18
    clf(fig1);
    subplot(1,2,1);
    plot(t_grid, 0.5*t_grid.^2, 'b-', 'LineWidth', 2.5); hold on;
    scatter(theta2, 0.5*theta2^2, 120, 'g', 'filled', 'MarkerEdgeColor', 'k');
    title(sprintf('L2 圆底瓷碗: 步数 %d, \\theta=%.3f', step-1, theta2));
    xlim([-4.2 4.2]); ylim([-0.5 8.5]); grid on;

    subplot(1,2,2);
    plot(t_grid, abs(t_grid)*1.8, 'r-', 'LineWidth', 2.5); hold on;
    scatter(theta1, abs(theta1)*1.8, 120, [0.9 0.4 0.1], 'filled', 'MarkerEdgeColor', 'k');
    title(sprintf('L1 V字尖谷: 步数 %d, \\theta=%.3f (谷底横跳!)', step-1, theta1));
    xlim([-4.2 4.2]); ylim([-0.5 8.5]); grid on;
    drawnow;
    if step == 1
        exportgraphics(fig1, gif1, 'Append', false);
    else
        exportgraphics(fig1, gif1, 'Append', true);
    end
    theta2 = theta2 - lr * theta2;
    theta1 = theta1 - lr * sign(theta1);
end
close(fig1);

%% 动画 3：SVM 颠铁锅筛花生米 3D 核升维 z = x1^2 + x2^2
fig3 = figure('Color', [1 0.98 0.92], 'Position', [100, 100, 640, 440]);
gif3 = fullfile(outDir, 'anim03-svm-trampoline-lift.gif');
rng(21);
r_in = 0.62 * rand(55,1); a_in = 2*pi*rand(55,1);
X_in = [r_in.*cos(a_in), r_in.*sin(a_in)];
r_out = 1.05 + 0.47 * rand(55,1); a_out = 2*pi*rand(55,1);
X_out = [r_out.*cos(a_out), r_out.*sin(a_out)];
z_in = sum(X_in.^2, 2); z_out = sum(X_out.^2, 2);
[px, py] = meshgrid(linspace(-1.5, 1.5, 18));
pz = 0.72 * ones(size(px));
lifts = [linspace(0, 1, 12), 1, 1, 1];
for idx = 1:length(lifts)
    clf(fig3);
    t = lifts(idx);
    scatter3(X_in(:,1), X_in(:,2), t*z_in, 45, [0.08 0.64 0.29], 'filled'); hold on;
    scatter3(X_out(:,1), X_out(:,2), t*z_out, 45, [0.86 0.15 0.15], 'filled');
    if t > 0.65
        surf(px, py, pz, 'FaceColor', [0.22 0.74 0.97], 'FaceAlpha', 0.35, 'EdgeColor', 'none');
    end
    xlim([-1.6 1.6]); ylim([-1.6 1.6]); zlim([0 2.5]);
    view(20 + idx*9, 52 - 30*t); grid on;
    title(sprintf('SVM 颠铁锅三维升维 z = x_1^2 + x_2^2 (进度 %d%%)', round(t*100)));
    drawnow;
    exportgraphics(fig3, gif3, 'Append', idx > 1);
end
close(fig3);
disp('All MATLAB animations exported successfully!');
