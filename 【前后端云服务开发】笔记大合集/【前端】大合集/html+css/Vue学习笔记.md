# Vue 学习笔记

[Vue.js - 渐进式 JavaScript 框架 | Vue.js](https://cn.vuejs.org/)

[Home | Vue CLI](https://cli.vuejs.org/zh/)



## Vue下载


```bash
cnpm install -g @vue/cli
```
![20260212213507](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212213507.png)
```bash
vue create vue-demo
```

选择自己配置（选第一个和第三个）


![20260212213533](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212213533.png)

```bash
cd vue-demo
```

```bash
cnpm run serve
```

![20260212213351](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212213351.png)

![20260212213558](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212213558.png)

成功了

## Vue入门



### 第一个Vue程序



```vue
<template>
  <div class="hello">
    <h1>学习Vue</h1>
    <p>{{ msg }}</p>
    <p v-html="rawHtml"></p>
    <p >{{ rawHtml }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: '关山难',
      rawHtml: "<a href='https://www.baidu.com'>百度</a>"
    }
  }
}
</script>

```

![20260212215541](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212215541.png)

## 打包发布一个静态页面



### 打包

```bash
 cd vue-demo1  
```



```bash
npm run build       
```

得到这样一个包

![20260212223004](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212223004.png)

### 添加站点

#### ![20260212223625](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212223625.png)







云解析

![20260212223314](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212223314.png)

### 上传

![20260212223503](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212223503.png)

### 设置伪静态



```nginx
location / {
    try_files $uri $uri/ /index.html;
}
```



访问网站



![20260212223825](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260212223825.png)