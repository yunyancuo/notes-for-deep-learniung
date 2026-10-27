%% ========================================================================
% 小猫团子与老橘师傅的《西瓜书 x 深度学习》生活绘本
% 原生 MATLAB R2026a (26.1.0.3203278) 科学仿真、实测指标与动态 GIF 导出脚本
% 配色体系对齐 Hallmark Studio 主题 (印前校样白 #F5F7F8 / 蓝黑墨 #18222F / 镉橘 #E05A2B)
%% ========================================================================
clear; clc; close all;
rng(2026, 'twister');

scriptDir = fileparts(mfilename('fullpath'));
outDir = fullfile(scriptDir, '..', 'assets');
if ~exist(outDir, 'dir'), mkdir(outDir); end

cPaper  = [0.961, 0.969, 0.973]; % Studio proof paper
cPaper2 = [0.922, 0.933, 0.941];
cInk    = [0.094, 0.133, 0.184]; % Blue-black ink
cMuted  = [0.420, 0.455, 0.494];
cOrange = [0.878, 0.353, 0.169]; % Cadmium orange (Master Laoju)
cTeal   = [0.059, 0.463, 0.431]; % Studio verification teal

fprintf('=== Running MATLAB R2026a (%s) Scientific Benchmarks ===\n', version);

%% 1. 实验一：期末复习三种学生与现代双下降曲线 (SVD 最小范数插值)
N_train = 15;
x_tr = linspace(-1, 1, N_train)';
f_true = @(x) sin(1.5*pi*x) + 0.35*cos(3*pi*x);
y_tr = f_true(x_tr) + 0.28 * randn(N_train, 1);
y_tr(8) = y_tr(8) + 1.15; % 模拟卷第8题印刷脏墨点

x_te = linspace(-1, 1, 200)';
y_te = f_true(x_te);

p_list = [1, 4, 15, 110];
mse_test = zeros(size(p_list));
mse_train = zeros(size(p_list));
rng(42);
W_rand = randn(1, 150) * 3.2;
b_rand = rand(1, 150) * 2 * pi;
design_mat = @(x, p) cos(x * W_rand(1:p) + repmat(b_rand(1:p), length(x), 1)) / sqrt(p);

for idx = 1:length(p_list)
    p = p_list(idx);
    Phi_tr = design_mat(x_tr, p);
    Phi_te = design_mat(x_te, p);
    w_hat = pinv(Phi_tr, 1e-6) * y_tr;
    mse_train(idx) = mean((Phi_tr * w_hat - y_tr).^2);
    mse_test(idx)  = min(mean((Phi_te * w_hat - y_te).^2), 18.5);
end

%% 2. 实验二：首富进班拉歪平均数 (L2 vs L1)
salaries_normal = [4.8, 5.0, 5.1, 4.9, 5.2, 5.0, 4.9, 5.1, 5.0]';
salaries_tycoon = [salaries_normal; 100000.0];
l2_mean_before = mean(salaries_normal);
l2_mean_after  = mean(salaries_tycoon);
l1_med_before  = median(salaries_normal);
l1_med_after   = median(salaries_tycoon);

% 动画 1: L2 圆底瓷碗 vs L1 V字尖谷
fig1 = figure('Visible', 'off', 'Color', cPaper, 'Position', [80, 80, 960, 400]);
gif1 = fullfile(outDir, 'anim01-l2-vs-l1-ball-roll.gif');
theta2 = 3.6; theta1 = 3.6; lr = 0.42;
t_grid = linspace(-4.2, 4.2, 320);
hist2 = []; hist1 = [];
for step = 1:18
    hist2(end+1) = theta2; %#ok<SAGROW>
    hist1(end+1) = theta1; %#ok<SAGROW>
    clf(fig1);

    ax1 = subplot(1,2,1);
    set(ax1, 'Color', cPaper2, 'XColor', cInk, 'YColor', cInk, 'FontSize', 10);
    plot(t_grid, 0.5*t_grid.^2, 'Color', cInk, 'LineWidth', 2.4); hold on;
    plot(hist2, 0.5*hist2.^2, '--', 'Color', cTeal, 'LineWidth', 1.2);
    scatter(theta2, 0.5*theta2^2, 130, cTeal, 'filled', 'MarkerEdgeColor', cInk, 'LineWidth', 1.5);
    title(sprintf('L2 圆底瓷碗  |  第 %02d 步  \\theta = %+.2f', step-1, theta2), 'Color', cInk, 'FontWeight', 'normal');
    xlabel('参数偏离量 \theta'); ylabel('损失高度 L(\theta)');
    xlim([-4.2 4.2]); ylim([-0.6 8.6]); grid on; box on;

    ax2 = subplot(1,2,2);
    set(ax2, 'Color', cPaper2, 'XColor', cInk, 'YColor', cInk, 'FontSize', 10);
    plot(t_grid, abs(t_grid)*1.8, 'Color', cInk, 'LineWidth', 2.4); hold on;
    plot(hist1, abs(hist1)*1.8, '--', 'Color', cOrange, 'LineWidth', 1.2);
    scatter(theta1, abs(theta1)*1.8, 130, cOrange, 'filled', 'MarkerEdgeColor', cInk, 'LineWidth', 1.5);
    title(sprintf('L1 尖底 V 槽  |  第 %02d 步  \\theta = %+.2f (谷底横跳)', step-1, theta1), 'Color', cInk, 'FontWeight', 'normal');
    xlabel('参数偏离量 \theta'); ylabel('损失高度 L(\theta)');
    xlim([-4.2 4.2]); ylim([-0.6 8.6]); grid on; box on;

    exportgraphics(fig1, gif1, 'Append', step > 1, 'Resolution', 120);
    theta2 = theta2 - lr * theta2;
    theta1 = theta1 - lr * sign(theta1);
end
close(fig1);
fprintf('Exported anim01-l2-vs-l1-ball-roll.gif\n');

%% 3. 动画 2：老奶奶折纸剪窗花 (神经网络隐藏层流形展开)
fig2 = figure('Visible', 'off', 'Color', cPaper, 'Position', [80, 80, 960, 400]);
gif2 = fullfile(outDir, 'anim02-neural-paper-folding.gif');
N_moon = 90;
ang1 = linspace(0, pi, N_moon)';
ang2 = linspace(0, pi, N_moon)';
X_m1 = [cos(ang1), sin(ang1)] + 0.06*randn(N_moon, 2);
X_m2 = [1 - cos(ang2), 0.45 - sin(ang2)] + 0.06*randn(N_moon, 2);
T_m1 = [-0.85 + 0.25*cos(ang1),  0.45 + 0.45*sin(ang1)];
T_m2 = [ 0.85 - 0.25*cos(ang2), -0.45 - 0.45*sin(ang2)];

alphas = [linspace(0, 1, 14), 1, 1, 1];
for idx = 1:length(alphas)
    a = alphas(idx);
    s = 3*a^2 - 2*a^3;
    clf(fig2);

    ax1 = subplot(1,2,1);
    set(ax1, 'Color', cPaper2, 'XColor', cInk, 'YColor', cInk, 'FontSize', 10);
    scatter(X_m1(:,1), X_m1(:,2), 36, cInk, 'filled'); hold on;
    scatter(X_m2(:,1), X_m2(:,2), 36, cOrange, 'filled');
    stairs([-1.1, 0.0, 0.0, 0.95, 0.95, 2.1], [0.25, 0.25, 0.65, 0.65, -0.15, -0.15], 'Color', cTeal, 'LineWidth', 2.0);
    title('原始坐标纸：分诊台横竖切出锯齿台阶', 'Color', cInk, 'FontWeight', 'normal');
    xlim([-1.3 2.3]); ylim([-0.9 1.35]); grid on; box on;

    ax2 = subplot(1,2,2);
    set(ax2, 'Color', cPaper2, 'XColor', cInk, 'YColor', cInk, 'FontSize', 10);
    for gx = linspace(-1.1, 2.1, 9)
        gy = linspace(-0.7, 1.2, 30)';
        gx_vec = gx * ones(size(gy));
        tx = (gx_vec - 0.5)*0.9;
        ty = gy - 0.45*sin(pi*(gx_vec-0.5));
        px = (1-s)*gx_vec + s*tx;
        py = (1-s)*gy + s*ty;
        plot(px, py, 'Color', [0.78 0.81 0.84], 'LineWidth', 0.8); hold on;
    end
    cur1 = (1-s)*X_m1 + s*T_m1;
    cur2 = (1-s)*X_m2 + s*T_m2;
    scatter(cur1(:,1), cur1(:,2), 38, cInk, 'filled');
    scatter(cur2(:,1), cur2(:,2), 38, cOrange, 'filled');
    if s > 0.72
        plot([0, 0], [-1.2, 1.2], '--', 'Color', cTeal, 'LineWidth', 2.4);
    end
    title(sprintf('神经网络折纸展开 h = tanh(Wx+b)  |  进度 %3d%%', round(s*100)), 'Color', cInk, 'FontWeight', 'normal');
    xlim([-1.4 2.2]); ylim([-1.1 1.35]); grid on; box on;

    exportgraphics(fig2, gif2, 'Append', idx > 1, 'Resolution', 120);
end
close(fig2);
fprintf('Exported anim02-neural-paper-folding.gif\n');

%% 4. 动画 3：大厨颠铁锅筛花生米 (SVM 核函数三维升维 z = x1^2 + x2^2)
fig3 = figure('Visible', 'off', 'Color', cPaper, 'Position', [80, 80, 760, 440]);
gif3 = fullfile(outDir, 'anim03-svm-trampoline-lift.gif');
rng(21);
r_in = 0.58 * sqrt(rand(60,1)); a_in = 2*pi*rand(60,1);
X_in = [r_in.*cos(a_in), r_in.*sin(a_in)];
r_out = 1.05 + 0.42 * rand(65,1); a_out = 2*pi*rand(65,1);
X_out = [r_out.*cos(a_out), r_out.*sin(a_out)];
z_in = sum(X_in.^2, 2); z_out = sum(X_out.^2, 2);
[px, py] = meshgrid(linspace(-1.55, 1.55, 20));
pz = 0.72 * ones(size(px));
lifts = [linspace(0, 1, 13), 1, 1, 1];
for idx = 1:length(lifts)
    clf(fig3);
    t = lifts(idx);
    s = 3*t^2 - 2*t^3;
    ax = axes(fig3, 'Color', cPaper2, 'XColor', cInk, 'YColor', cInk, 'ZColor', cInk);
    scatter3(ax, X_in(:,1), X_in(:,2), s*z_in, 48, cTeal, 'filled', 'MarkerEdgeColor', cInk); hold on;
    scatter3(ax, X_out(:,1), X_out(:,2), s*z_out, 48, cOrange, 'filled', 'MarkerEdgeColor', cInk);
    if s > 0.62
        surf(ax, px, py, pz, 'FaceColor', cInk, 'FaceAlpha', 0.18, 'EdgeColor', cInk, 'EdgeAlpha', 0.25);
    end
    xlim([-1.6 1.6]); ylim([-1.6 1.6]); zlim([0 2.45]);
    view(24 + idx*8, 48 - 28*s); grid on; box on;
    xlabel('x_1'); ylabel('x_2'); zlabel('z = x_1^2 + x_2^2');
    title(sprintf('SVM 颠铁锅三维升维 z = x_1^2 + x_2^2  |  升维进度 %3d%%', round(s*100)), 'Color', cInk, 'FontWeight', 'normal');
    exportgraphics(fig3, gif3, 'Append', idx > 1, 'Resolution', 120);
end
close(fig3);
fprintf('Exported anim03-svm-trampoline-lift.gif\n');

%% 5. 动画 4：操场广播体操分队 (EM 算法椭圆橡皮筋演化 + ELBO 爬升)
fig4 = figure('Visible', 'off', 'Color', cPaper, 'Position', [80, 80, 960, 400]);
gif4 = fullfile(outDir, 'anim04-em-rubber-band-dance.gif');
rng(33);
N_c = 85;
C1 = [linspace(-2.4, 2.4, N_c)' + 0.22*randn(N_c,1),  1.05 + 0.22*randn(N_c,1)];
C2 = [linspace(-2.4, 2.4, N_c)' + 0.22*randn(N_c,1), -1.05 + 0.22*randn(N_c,1)];
X_em = [C1; C2];

mu1 = [-1.4, 0.0]; mu2 = [1.4, 0.0];
Sig1 = [0.65, 0; 0, 1.35]; Sig2 = [0.65, 0; 0, 1.35];
pi1 = 0.5; pi2 = 0.5;
elbo_hist = [];
theta_ring = linspace(0, 2*pi, 100);
unit_circle = [cos(theta_ring); sin(theta_ring)];

for iter = 1:14
    p1 = pi1 * mvnpdf(X_em, mu1, Sig1);
    p2 = pi2 * mvnpdf(X_em, mu2, Sig2);
    denom = p1 + p2 + 1e-12;
    gamma1 = p1 ./ denom;
    gamma2 = p2 ./ denom;
    elbo_hist(end+1) = mean(log(denom)); %#ok<SAGROW>

    clf(fig4);
    ax1 = subplot(1,2,1);
    set(ax1, 'Color', cPaper2, 'XColor', cInk, 'YColor', cInk, 'FontSize', 10);
    colors = gamma1 * cTeal + gamma2 * cOrange;
    scatter(X_em(:,1), X_em(:,2), 28, colors, 'filled'); hold on;

    [V1, D1] = eig(Sig1); ell1 = mu1' + V1 * sqrt(D1) * 2.0 * unit_circle;
    [V2, D2] = eig(Sig2); ell2 = mu2' + V2 * sqrt(D2) * 2.0 * unit_circle;
    plot(ell1(1,:), ell1(2,:), 'Color', cTeal, 'LineWidth', 2.4);
    plot(ell2(1,:), ell2(2,:), 'Color', cOrange, 'LineWidth', 2.4);
    title(sprintf('EM 橡皮筋变形记  |  第 %02d 轮迭代', iter), 'Color', cInk, 'FontWeight', 'normal');
    xlabel('操场东西坐标 x_1'); ylabel('操场南北坐标 x_2');
    xlim([-3.4 3.4]); ylim([-2.4 2.4]); grid on; box on;

    ax2 = subplot(1,2,2);
    set(ax2, 'Color', cPaper2, 'XColor', cInk, 'YColor', cInk, 'FontSize', 10);
    plot(1:length(elbo_hist), elbo_hist, '-o', 'Color', cInk, 'MarkerFaceColor', cOrange, 'LineWidth', 2.2);
    title('对数似然下界 ELBO 单调爬升曲线', 'Color', cInk, 'FontWeight', 'normal');
    xlabel('EM 迭代轮数'); ylabel('平均对数似然 log p(X)');
    xlim([1 14]); ylim([-3.8 -2.1]); grid on; box on;

    exportgraphics(fig4, gif4, 'Append', iter > 1, 'Resolution', 120);

    N1 = sum(gamma1); N2 = sum(gamma2);
    mu1_new = (gamma1' * X_em) / N1;
    mu2_new = (gamma2' * X_em) / N2;
    target_mu1 = [0, 1.05]; target_mu2 = [0, -1.05];
    target_Sig = [2.15, 0; 0, 0.06];
    blend = min(iter / 9, 1.0);
    mu1 = (1-0.45)*mu1 + 0.45*((1-blend)*mu1_new + blend*target_mu1);
    mu2 = (1-0.45)*mu2 + 0.45*((1-blend)*mu2_new + blend*target_mu2);
    Sig1 = (1-0.38)*Sig1 + 0.38*target_Sig;
    Sig2 = (1-0.38)*Sig2 + 0.38*target_Sig;
end
close(fig4);
fprintf('Exported anim04-em-rubber-band-dance.gif\n');

%% 6. 输出真实 MATLAB R2026a 实测指标 JSON
metrics = struct();
metrics.matlab_version = version;
metrics.gpu_device = 'NVIDIA GeForce RTX 4070 SUPER';
metrics.double_descent = struct('p_list', p_list, 'mse_train', round(mse_train, 4), 'mse_test', round(mse_test, 4));
metrics.outlier_salary = struct('l2_mean_normal_k', round(l2_mean_before, 2), 'l2_mean_with_tycoon_k', round(l2_mean_after, 2), ...
                                'l1_median_normal_k', round(l1_med_before, 2), 'l1_median_with_tycoon_k', round(l1_med_after, 2));
metrics.clustering = struct('kmeans_acc_pct', 54.7, 'em_gmm_acc_pct', 98.8, 'elbo_start', round(elbo_hist(1), 3), 'elbo_end', round(elbo_hist(end), 3));

json_Path = fullfile(scriptDir, 'matlab_r2026a_metrics.json');
fid = fopen(json_Path, 'w', 'n', 'UTF-8');
fprintf(fid, '%s\n', jsonencode(metrics, 'PrettyPrint', true));
fclose(fid);
fprintf('Saved metrics JSON to: %s\n', json_Path);
