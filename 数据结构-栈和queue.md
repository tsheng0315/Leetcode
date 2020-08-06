## 栈与队列

栈/队列是比较特殊的线性表.

因为对于栈来说，访问、插入和删除元素只能在栈顶进行;

对于queue来说，元素只能从队列尾插入，从队列头访问和删除。

## 栈

栈是限制插入和删除只能在一个位置上进行的表，该位置是表的末端，叫作栈顶。

栈叫作LIFO(Last In First Out)

对栈的基本操作有push(进栈)和pop(出栈)，前者相当于插入，后者相当于删除最后一个元素。

![](https://upload-images.jianshu.io/upload_images/2243690-2e9540a7b4b61cbd.png?imageMogr2/auto-orient/strip|imageView2/2/w/220/format/webp)


## queue:

队列是一种特殊的线性表. 

它只允许在表的前端（front）进行删除操作，在表的后端（rear）进行插入操作. 

进行插入操作的端称为队尾，进行删除操作的端称为队头。

![](https://upload-images.jianshu.io/upload_images/2243690-3116f05bb106b789.png?imageMogr2/auto-orient/strip|imageView2/2/w/446/format/webp)


## priority queue

priority queue中，元素都被赋予优先级。当访问元素的时候，具有最高优先级的元素最先被删除。

优先队列在生活中的应用: 比如医院的急症室为病人赋予优先级，最高优先级的病人最先治疗
