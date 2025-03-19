/*
白色模式下显示方块背景
*/
window.addEventListener('resize', sizeChange);
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
sizeChange()
function sizeChange() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    if (canvas.width<667){
        var num=5;
    }else{
        num=10;
    };
    //晶格大小
    boxSize = (canvas.width / num);
    //横向晶格数量
    xBoxIength = (canvas.width / boxSize).toFixed() + 1
    //纵向晶格数量
    yBoxIength = (canvas.height / boxSize).toFixed()+ 1
    angle = 0;
    unitangle=Math.PI/100
    polygonVertices = []
    //列出晶格起点
    for (let i = 0; i < xBoxIength; i++) {
        for (let j = 0; j < yBoxIength; j++) {
            let polygon = {
                x: i * boxSize,
                y: j * boxSize,
                color: Math.random() * 2 * Math.PI
            }
            polygonVertices.push(polygon)
        }
    };
}
//抗锯齿
ctx.imageSmoothingEnabled = false;

function drawPolygon() {
    //清理画布
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    //开始路径
    ctx.beginPath();
    //动画规则(x0,y0)(x1,y1)
    for (idoc of polygonVertices) {
        //1
        const x00 = idoc.x;
        const y00 = idoc.y;
        //2
        const x10 = idoc.x + boxSize;
        const y10 = idoc.y;
        //3
        const x01 = idoc.x;
        const y01 = idoc.y + boxSize;
        //4
        const x11 = idoc.x + boxSize;
        const y11 = idoc.y + boxSize;
        //开始路径
        ctx.beginPath();
        ctx.moveTo(x00, y00);

        ctx.lineTo(x10, y10);
        ctx.lineTo(x11, y11);
        ctx.lineTo(x01, y01);

        ctx.closePath();
        ctx.fillStyle = `rgba(236, 239, 241, ${colorAdd(idoc.color + angle)})`;
        ctx.fill();
    }
    
    angle =(angle+unitangle)%(2*Math.PI);
}
function colorAdd(value) {
    return ((Math.cos(value) / 4) + 0.75)
}
function animate() {
    drawPolygon();
    requestAnimationFrame(animate);
}
animate();