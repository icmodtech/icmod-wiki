//获取url
const url_language_select =window.location.href
// 获取语言选择元素
const link = document.querySelectorAll('.md-select__link');
// 拆分 URL 成数组
var parts = url_language_select.split('/');
// 删除域名部分
parts.splice(0, 3);
// 重新拼接 URL
var newHref = parts.join('/');
// 设置新的 href 值
for (var i = 0; i < link.length; i++) {
    // 获取当前 href 值
    var currentHref = link[i].href;
    link[i].href = currentHref+newHref;
}