from website.article_prelude import *

title = "自造编程语言2026"
date = datetime(2026, 5, 26, tzinfo=ZoneInfo("Asia/Shanghai"))
content = """
@Paragraph
    挺久没有想过自己想设计什么流派的编程语言了。
@@
@Paragraph
    最核心的是垃圾收集和重度闭包使用。
    LISP教会我们闭包是多种高价值抽象的最简实现的基础。
    @SideNote
        说到这里，也应该注意一下不要过度追求极简。
    @@
    写Rust多了就会怀念可以无忧无虑用闭包随便捕获变量的感觉。
    算是职业病药方。
@@
@Paragraph
    以前高度倾向于动态类型解释执行，现在有点想做强类型了，喜欢写会被编译掉的代码。
    两者兼具就是解释执行+即时编译。
    想把看似静态的语言特性做到运行时执行去。
    把Rust的过程宏做成在程序开始执行时在载入程序的过程中执行。
    @CodeBlock
        plaintext
        define type MyType { ... }
        derive_debug(MyType)
        // 或者提供语法支持
        derive Debug for MyType
        // 还有泛型
        define function List(T Type) Type {
            define type TheList {
                head: T
                tail: TheList
            }
            define function new(head: T, tail: TheList) -> TheList { ... }
            ...
        }
        define type IntList = List(Int)
        let l = IntList.new(...)
    @@
    这大概率意味着结构化类型：所有的
    @Code
        List(Int)
    @@
    都解析到同一个类型上，只执行泛型类型函数一次。
    不知道这些设计有什么优势，只是觉得很酷。
@@
@Paragraph
    太动态了可能会给实现开发环境带来挑战。
    语言服务器应该始终都在增量编译，编译的主要目的是提供语言服务，编译的所谓产物只是语言服务的副产品，需要的时候导出/下载一下。
    编译的过程就是就是把顶层语句执行一遍，最后不要调用入口函数（如果有）就行。
@@
@Paragraph
    这几年来想的最多的异步特性倒是没太在意了。
    异步肯定要有，而且要有多态特性避免染色（不然重度闭包使用就要完蛋了），但是具体怎么做再说吧。
    你有这么灵活的运行时类型系统进入语言，应该是不愁这些了。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page(Path(__file__).stem, page)