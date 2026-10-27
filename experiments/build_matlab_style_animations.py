# -*- coding: utf-8 -*-
"""
生成 4 张 MATLAB 风格科学动态 GIF 动画 (assets/anim01 ~ anim04.gif)
配合【小猫团子 & 老橘师傅】的生活化例子，在 GitHub README 与 Jupyter 中直接循环播放！
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import io

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.facecolor'] = '#FFFBEB'
plt.rcParams['axes.facecolor'] = '#FFFFFF'

ROOT = r'C:\Users\34684\Documents\notes-for-deep-learniung'
ASSETS = os.path.join(ROOT, 'assets')
os.makedirs(ASSETS, exist_ok=True)


def fig_to_pil(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=105, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert('P', palette=Image.ADAPTIVE, colors=128)


def save_gif(frames, filename, duration=140):
    path = os.path.join(ASSETS, filename)
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=duration,
        loop=0
    )
    size_kb = os.path.getsize(path) / 1024
    print(f"Saved animated GIF: {filename} ({len(frames)} frames, {size_kb:.1f} KB)")


# ==============================================================================
# 动画 1：圆碗滚珠 vs V字尖谷反复横跳 (复现《线性神经网络.ipynb》L2 vs L1 驻点震荡)
# ==============================================================================
def build_anim01():
    theta_l2, theta_l1 = 3.6, 3.6
    lr = 0.42
    hist_l2, hist_l1 = [theta_l2], [theta_l1]
    for _ in range(17):
        theta_l2 = theta_l2 - lr * theta_l2
        theta_l1 = theta_l1 - lr * np.sign(theta_l1)
        hist_l2.append(theta_l2)
        hist_l1.append(theta_l1)

    t_grid = np.linspace(-4.2, 4.2, 300)
    frames = []
    for step in range(len(hist_l2)):
        fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0))
        fig.suptitle(f'[动态实验 1] 碗底滚玻璃珠 (L2丝滑停稳) vs 尖底峡谷 (L1反复横跳)  [第 {step:02d}/17 步]',
                     fontsize=13, fontweight='bold', color='#78350F', y=1.02)

        # 左图：L2 圆碗
        ax = axes[0]
        ax.plot(t_grid, 0.5 * t_grid**2, color='#2563EB', lw=2.8, label='L2 平滑圆碗: 越近谷底坡越缓')
        past_x = np.array(hist_l2[:step+1])
        ax.plot(past_x, 0.5 * past_x**2, 'o--', color='#93C5FD', markersize=5, lw=1.5)
        cur_x = hist_l2[step]
        ax.scatter([cur_x], [0.5 * cur_x**2], c='#16A34A', s=150, zorder=6, edgecolors='black', lw=1.5,
                   label=f'当前玻璃珠位置 θ = {cur_x:+.3f}')
        ax.set_xlim(-4.2, 4.2); ax.set_ylim(-0.5, 8.5)
        ax.set_title('① L2 平方误差：像圆底瓷碗，稳稳停在碗底 0 点', fontsize=11, fontweight='bold')
        ax.set_xlabel('参数偏离 θ'); ax.set_ylabel('损失高度 L(θ)')
        ax.legend(loc='upper center', fontsize=9)
        ax.grid(True, linestyle='--', alpha=0.6)

        # 右图：L1 V字尖谷
        ax = axes[1]
        ax.plot(t_grid, np.abs(t_grid) * 1.8, color='#DC2626', lw=2.8, label='L1 尖底V字谷: 左右坡度恒为 ±1')
        past_x1 = np.array(hist_l1[:step+1])
        ax.plot(past_x1, np.abs(past_x1) * 1.8, 'o--', color='#FCA5A5', markersize=5, lw=1.5)
        cur_x1 = hist_l1[step]
        ax.scatter([cur_x1], [np.abs(cur_x1) * 1.8], c='#EA580C', s=150, zorder=6, edgecolors='black', lw=1.5,
                   label=f'当前玻璃珠位置 θ = {cur_x1:+.3f}')
        ax.set_xlim(-4.2, 4.2); ax.set_ylim(-0.5, 8.5)
        ax.set_title('② L1 绝对值误差：步长固定时在谷底永远左右横跳！', fontsize=11, fontweight='bold')
        ax.set_xlabel('参数偏离 θ'); ax.set_ylabel('损失高度 L(θ)')
        ax.legend(loc='upper center', fontsize=9)
        ax.grid(True, linestyle='--', alpha=0.6)

        fig.tight_layout()
        frames.append(fig_to_pil(fig))
    save_gif(frames, 'anim01-l2-vs-l1-ball-roll.gif', duration=180)


# ==============================================================================
# 动画 2：折纸剪窗花慢动作回放 (神经网络隐藏层如何把双月牙一步步拉开拉直)
# ==============================================================================
def build_anim02():
    np.random.seed(12)
    N_half = 70
    t1 = np.linspace(0, np.pi, N_half)
    t2 = np.linspace(0, np.pi, N_half)
    X1 = np.column_stack([np.cos(t1), np.sin(t1)]) + np.random.normal(0, 0.09, (N_half, 2))
    X2 = np.column_stack([1.0 - np.cos(t2), 0.45 - np.sin(t2)]) + np.random.normal(0, 0.09, (N_half, 2))
    X = np.vstack([X1, X2])
    y = np.hstack([np.zeros(N_half, dtype=int), np.ones(N_half, dtype=int)])

    # 训练 2 层网络获得展开后的 2D 坐标 A2
    np.random.seed(7)
    H = 16
    W1 = np.random.randn(2, H) * 1.4; b1 = np.zeros((1, H))
    W2 = np.random.randn(H, 2) * 0.6; b2 = np.zeros((1, 2))
    W3 = np.random.randn(2, 1) * 0.8; b3 = np.zeros((1, 1))
    y_col = y[:, None].astype(float)
    lr = 0.08
    for _ in range(900):
        Z1 = X @ W1 + b1; A1 = np.maximum(0, Z1)
        Z2 = A1 @ W2 + b2; A2 = np.tanh(Z2)
        logits = A2 @ W3 + b3
        prob = 1.0 / (1.0 + np.exp(-np.clip(logits, -15, 15)))
        dlogits = (prob - y_col) / len(X)
        dW3 = A2.T @ dlogits; db3 = np.sum(dlogits, axis=0, keepdims=True)
        dA2 = dlogits @ W3.T; dZ2 = dA2 * (1.0 - A2 ** 2)
        dW2 = A1.T @ dZ2; db2 = np.sum(dZ2, axis=0, keepdims=True)
        dA1 = dZ2 @ W2.T; dZ1 = dA1 * (Z1 > 0)
        dW1 = X.T @ dZ1; db1 = np.sum(dZ1, axis=0, keepdims=True)
        W1 -= lr * dW1; b1 -= lr * db1
        W2 -= lr * dW2; b2 -= lr * db2
        W3 -= lr * dW3; b3 -= lr * db3

    # 归一化原坐标 X_norm 到 [-1, 1] 方便平滑插值过渡到 A2
    X_norm = (X - X.mean(axis=0)) / (X.std(axis=0) * 1.3)
    # 变形网格背景线
    gx, gy = np.meshgrid(np.linspace(-1.3, 2.2, 12), np.linspace(-0.8, 1.3, 12))
    g_pts = np.column_stack([gx.ravel(), gy.ravel()])
    g_norm = (g_pts - X.mean(axis=0)) / (X.std(axis=0) * 1.3)
    g_a2 = np.tanh(np.maximum(0, g_pts @ W1 + b1) @ W2 + b2)

    alphas = np.concatenate([np.linspace(0, 1, 14), [1.0, 1.0, 1.0]])
    frames = []
    for idx, alpha in enumerate(alphas):
        fig, ax = plt.subplots(figsize=(6.8, 4.5))
        cur_pts = (1 - alpha) * X_norm + alpha * A2
        cur_grid = (1 - alpha) * g_norm + alpha * g_a2

        # 画橡皮纸网格变形
        cur_gx = cur_grid[:, 0].reshape(gx.shape)
        cur_gy = cur_grid[:, 1].reshape(gy.shape)
        for r in range(gx.shape[0]):
            ax.plot(cur_gx[r, :], cur_gy[r, :], color='#CBD5E1', lw=0.8, zorder=1)
        for c in range(gx.shape[1]):
            ax.plot(cur_gx[:, c], cur_gy[:, c], color='#CBD5E1', lw=0.8, zorder=1)

        ax.scatter(cur_pts[y == 0, 0], cur_pts[y == 0, 1], c='#2563EB', s=42, edgecolors='white', lw=0.6, zorder=4, label='蓝花图案 (类别 A)')
        ax.scatter(cur_pts[y == 1, 0], cur_pts[y == 1, 1], c='#DC2626', s=42, edgecolors='white', lw=0.6, zorder=4, label='红花图案 (类别 B)')

        if alpha > 0.75:
            h1_v = np.linspace(-1.1, 1.1, 100)
            h2_v = -(W3[0, 0] * h1_v + b3[0, 0]) / (W3[1, 0] + 1e-8)
            ax.plot(h1_v, h2_v, 'g--', lw=3.0, zorder=5, label='[剪刀线] 折好后直着剪一刀就彻底分开！')

        ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.35, 1.35)
        stage_txt = "原图：红蓝月牙拧成麻花，直剪刀剪不开" if alpha < 0.2 else (
            f"隐藏层正在折纸拉平空间... (展开进度 {int(alpha*100)}%)" if alpha < 0.95 else "[完成] 折纸完成！红蓝分列两边，一刀笔直剪开！"
        )
        ax.set_title(f'[动态实验 2] 神经网络“折纸剪窗花”慢动作\n{stage_txt}', fontsize=11.5, fontweight='bold', color='#1E3A8A')
        ax.legend(loc='lower left', fontsize=9)
        fig.tight_layout()
        frames.append(fig_to_pil(fig))
    save_gif(frames, 'anim02-neural-paper-folding.gif', duration=160)


# ==============================================================================
# 动画 3：颠铁锅筛花生米 3D 慢动作升维 (SVM 核函数升维 z = x1^2 + x2^2)
# ==============================================================================
def build_anim03():
    np.random.seed(21)
    N_ring = 55
    r_in = np.random.uniform(0.0, 0.62, N_ring)
    ang_in = np.random.uniform(0, 2 * np.pi, N_ring)
    X_in = np.column_stack([r_in * np.cos(ang_in), r_in * np.sin(ang_in)])
    r_out = np.random.uniform(1.05, 1.52, N_ring)
    ang_out = np.random.uniform(0, 2 * np.pi, N_ring)
    X_out = np.column_stack([r_out * np.cos(ang_out), r_out * np.sin(ang_out)])

    z_in_full = X_in[:, 0]**2 + X_in[:, 1]**2
    z_out_full = X_out[:, 0]**2 + X_out[:, 1]**2

    px, py = np.meshgrid(np.linspace(-1.55, 1.55, 18), np.linspace(-1.55, 1.55, 18))
    pz = np.ones_like(px) * 0.72

    lifts = np.concatenate([np.linspace(0, 1.0, 12), [1.0, 1.0, 1.0, 1.0]])
    frames = []
    for idx, t in enumerate(lifts):
        fig = plt.figure(figsize=(6.8, 4.6))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X_in[:, 0], X_in[:, 1], t * z_in_full, c='#16A34A', s=32, label='内圈绿豆 (留在锅底)')
        ax.scatter(X_out[:, 0], X_out[:, 1], t * z_out_full, c='#DC2626', s=32, label='外圈花生皮 (颠上高空!)')

        if t > 0.65:
            ax.plot_surface(px, py, pz, color='#38BDF8', alpha=0.35)

        ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6); ax.set_zlim(0, 2.5)
        ax.view_init(elev=52 - 30 * t, azim=20 + idx * 9)
        msg = "平底盘里：花生皮围住绿豆，怎么画直线都分不开" if t < 0.2 else (
            f"正在往上颠铁锅升维 z=x1^2+x2^2... ({int(t*100)}%)" if t < 0.85 else "[完成] 飞到半空啦！拿蓝色硬纸板从中间平插一刀搞定！"
        )
        ax.set_title(f'[动态实验 3] SVM“颠铁锅筛花生米”三维核升维\n{msg}', fontsize=11, fontweight='bold', color='#065F46')
        ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('高度 z')
        ax.legend(loc='upper left', fontsize=8.5)
        fig.tight_layout()
        frames.append(fig_to_pil(fig))
    save_gif(frames, 'anim03-svm-trampoline-lift.gif', duration=160)


# ==============================================================================
# 动画 4：操场广播体操分队 (EM 算法椭圆橡皮筋 15 轮动态变形与 ELBO 爬山)
# ==============================================================================
def build_anim04():
    from scipy.stats import multivariate_normal
    np.random.seed(18)
    N1, N2 = 100, 100
    cov1 = np.array([[2.2, 1.35], [1.35, 0.95]])
    cov2 = np.array([[1.8, -1.1], [-1.1, 0.85]])
    X1 = np.random.multivariate_normal([0.0, 1.3], cov1, N1)
    X2 = np.random.multivariate_normal([1.6, -0.6], cov2, N2)
    X = np.vstack([X1, X2])

    pi_k = np.array([0.5, 0.5])
    mu_k = np.array([[-1.4, -0.4], [2.4, 0.8]])
    sig_k = np.array([np.eye(2) * 1.6, np.eye(2) * 1.6])
    log_liks = []

    gx, gy = np.meshgrid(np.linspace(-3.5, 5.0, 80), np.linspace(-3.0, 4.0, 80))
    gpts = np.column_stack([gx.ravel(), gy.ravel()])

    frames = []
    for step in range(1, 15):
        p0 = pi_k[0] * multivariate_normal.pdf(X, mu_k[0], sig_k[0])
        p1 = pi_k[1] * multivariate_normal.pdf(X, mu_k[1], sig_k[1])
        total_p = p0 + p1 + 1e-15
        log_liks.append(np.sum(np.log(total_p)))
        gamma0 = p0 / total_p
        gamma1 = p1 / total_p

        fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.1))
        fig.suptitle(f'[动态实验 4] 操场体操分队 EM 橡皮筋变形记  [第 {step:02d}/14 轮：先猜人(E步) -> 再拉长橡皮筋(M步)]',
                     fontsize=12.5, fontweight='bold', color='#78350F', y=1.02)

        ax = axes[0]
        lbl = (gamma1 > gamma0).astype(int)
        ax.scatter(X[lbl == 0, 0], X[lbl == 0, 1], c='#2563EB', s=24, alpha=0.8, label='猜为一班同学')
        ax.scatter(X[lbl == 1, 0], X[lbl == 1, 1], c='#16A34A', s=24, alpha=0.8, label='猜为二班同学')
        z0 = multivariate_normal.pdf(gpts, mu_k[0], sig_k[0]).reshape(gx.shape)
        z1 = multivariate_normal.pdf(gpts, mu_k[1], sig_k[1]).reshape(gx.shape)
        ax.contour(gx, gy, z0, levels=3, colors='#1D4ED8', linewidths=2.0)
        ax.contour(gx, gy, z1, levels=3, colors='#15803D', linewidths=2.0)
        ax.set_xlim(-3.5, 5.0); ax.set_ylim(-3.0, 4.0)
        ax.set_title('① 两条橡皮筋顺着长条队形自动拉长变扁！', fontsize=11, fontweight='bold')
        ax.set_xlabel('操场横坐标 x1'); ax.set_ylabel('操场纵坐标 x2')
        ax.legend(loc='lower left', fontsize=8.5)
        ax.grid(True, linestyle='--', alpha=0.6)

        ax2 = axes[1]
        ax2.plot(range(1, len(log_liks)+1), log_liks, 'o-', color='#7C3AED', lw=2.6, markersize=6, label='对数似然得分 (ELBO)')
        ax2.set_xlim(1, 14); ax2.set_ylim(-760, -640)
        ax2.set_title('② 搭梯子爬山 (ELBO)：每一轮得分严格往上涨！', fontsize=11, fontweight='bold')
        ax2.set_xlabel('EM 来回调整轮数'); ax2.set_ylabel('贴合度总分 log P(X|θ)')
        ax2.legend(loc='lower right', fontsize=9)
        ax2.grid(True, linestyle='--', alpha=0.6)

        fig.tight_layout()
        frames.append(fig_to_pil(fig))

        # M 步更新
        N_k0, N_k1 = np.sum(gamma0), np.sum(gamma1)
        pi_k = np.array([N_k0, N_k1]) / len(X)
        mu_k[0] = (gamma0[:, None] * X).sum(axis=0) / N_k0
        mu_k[1] = (gamma1[:, None] * X).sum(axis=0) / N_k1
        dX0 = X - mu_k[0]; dX1 = X - mu_k[1]
        sig_k[0] = (dX0.T @ (gamma0[:, None] * dX0)) / N_k0 + np.eye(2) * 1e-4
        sig_k[1] = (dX1.T @ (gamma1[:, None] * dX1)) / N_k1 + np.eye(2) * 1e-4

    save_gif(frames, 'anim04-em-rubber-band-dance.gif', duration=200)


if __name__ == '__main__':
    build_anim01()
    build_anim02()
    build_anim03()
    build_anim04()
