// 粒子数量，每次点击发射的粒子数量，可调整
const numParticlesPerClick = 10;
// 粒子的最小尺寸和最大尺寸（单位：px），这里可以根据图片实际尺寸调整
const minSize = 8;
const maxSize = 15;
// 粒子初始垂直方向速度范围（单位：px/帧，朝上为正方向），调整初速度大小范围
const minInitialSpeedY = 5;
const maxInitialSpeedY = 10;
// 粒子水平方向速度范围（单位：px/帧）
const minSpeedX = -3;
const maxSpeedX = 3;
// 重力加速度（单位：px/帧²，模拟现实中重力效果，方向朝下为正）
const gravity = -0.5;
// 粒子最大存活时间（单位：帧，用于控制粒子短时间内随机消失，避免性能问题）
const maxLifetime = 60;

// 图片分割的行数和列数，用于模拟不同图片，可根据想要的不同样式数量调整
const rows = 2;
const cols = 2;

// 创建粒子元素并设置初始属性的函数
function createParticle(x, y) {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    const size = Math.random() * (maxSize - minSize) + minSize;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.backgroundSize = 'contain';
    particle.style.backgroundRepeat = 'no-repeat';
    // 计算每个小方块在整张图片中的位置（通过行列索引）
    const rowIndex = Math.floor(Math.random() * rows);
    const colIndex = Math.floor(Math.random() * cols);
    const offsetX = (colIndex / cols) * 100;
    const offsetY = (rowIndex / rows) * 100;
    particle.style.backgroundPosition = `${offsetX}% ${offsetY}%`;
    particle.style.backgroundImage = `url('dirt.png')`;
    particle.style.left = `${x}px`;
    particle.style.top = `${y}px`;
    // 初始垂直方向速度朝上，随机生成在设定范围内
    const initialSpeedY = Math.random() * (maxInitialSpeedY - minInitialSpeedY) + minInitialSpeedY;
    const speedX = Math.random() * (maxSpeedX - minSpeedX) + minSpeedX;
    particle.dataset.speedX = speedX;
    particle.dataset.speedY = -initialSpeedY;
    particle.dataset.lifetime = 0;
    document.body.appendChild(particle);
    return particle;
}

// 更新粒子位置，实现粒子运动效果并考虑重力和粒子存活时间
function updateParticles() {
    const particles = document.querySelectorAll('.particle');
    particles.forEach(particle => {
        const currentX = parseInt(particle.style.left, 10);
        const currentY = parseInt(particle.style.top, 10);
        const speedX = parseFloat(particle.dataset.speedX);
        const speedY = parseFloat(particle.dataset.speedY);
        const lifetime = parseInt(particle.dataset.lifetime, 10);
        // 根据重力加速度更新垂直方向速度
        const newSpeedY = speedY - gravity;
        particle.dataset.speedY = newSpeedY;
        particle.style.left = `${currentX + speedX}px`;
        particle.style.top = `${currentY + speedY}px`;
        particle.dataset.lifetime = lifetime + 1;
        // 判断粒子是否超出页面范围或者达到最大存活时间，如果满足则移除粒子
        if (currentX < -10 || currentX > window.innerWidth + 10 || currentY < -10 || currentY > window.innerHeight + 10 || lifetime >= maxLifetime) {
            particle.remove();
        }
    });
    requestAnimationFrame(updateParticles);
}

// 页面加载完成后开始更新粒子位置
window.addEventListener('load', () => {
    requestAnimationFrame(updateParticles);
});

// 监听页面点击事件，在点击位置发射粒子
document.addEventListener('click', (event) => {
    for (let i = 0; i < numParticlesPerClick; i++) {
        createParticle(event.pageX, event.pageY);
    }
});