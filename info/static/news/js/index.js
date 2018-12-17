var currentCid = 1; // 当前分类 id
var cur_page = 1; // 当前页
var total_page = 1;  // 总页数
var data_querying = true;   // 是否正在向后台获取数据


$(function () {
    //界面加载完成之后加载新闻页面
    updateNewsData()

    // 首页分类切换
    $('.menu li').click(function () {
        // 取到指定分类的cid
        var clickCid = $(this).attr('data-cid')
        // 遍历所有的li移除身上的选中效果
        $('.menu li').each(function () {
            $(this).removeClass('active')
        })
        //给当前分类添加选中的状态
        $(this).addClass('active')
            //如果点击的分类与当前分类不一致

        if (clickCid != currentCid) {
            // 记录当前分类id
            currentCid = clickCid

            // 重置分页参数
            cur_page = 1
            total_page = 1
            updateNewsData()
        }
    })

    //页面滚动加载相关
    $(window).scroll(function () {

        // 浏览器窗口高度
        var showHeight = $(window).height();

        // 整个网页的高度
        var pageHeight = $(document).height();

        // 页面可以滚动的距离
        var canScrollHeight = pageHeight - showHeight;

        // 页面滚动了多少,这个是随着页面滚动实时变化的
        var nowScroll = $(document).scrollTop();

        if ((canScrollHeight - nowScroll) < 100) {
            // TODO 判断页数，去更新新闻数据
            // console.log("滚动到底部了")
            if (!data_querying) {
            // 将`是否正在向后端查询新闻数据`的标志设置为真
                data_querying = true;
            // 如果当前页面数还没到达总页数
                if(cur_page < total_page) {
                // 向后端发送请求，查询下一页新闻数据
                    cur_page += 1;
                updateNewsData();
            } else {
                data_querying = false;
            }
        }
        }
    })
})

function updateNewsData() {
    // TODO 更新新闻数据
    var params = {
        "cid": currentCid,
        "page": cur_page,
        "per_page": 50
    }

    $.get("/news_list", params, function (resp) {
        //数据加载完毕，设置  正在加载数据 的变量为false，代表当前没有在加载数据
        data_querying = false
        if (resp.errno == "0"){

            total_page = resp.data.total_page

            if (cur_page == 1){
                $(".list_con").html("")
            }
            //请求成功,清除已有数据


            // 显示数据
            // alert(resp.data.news_dict_li[1].index_image_url)
            for (var i=0;i<resp.data.news_dict_li.length;i++) {

                var news = resp.data.news_dict_li[i]

                var content = '<li>'
                content += '<a href="#" class="news_pic fl"><img src="' + news.index_image_url + '?imageView2/1/w/170/h/170"></a>'
                content += '<a href="#" class="news_title fl">' + news.title + '</a>'
                content += '<a href="#" class="news_detail fl">' + news.digest + '</a>'
                content += '<div class="author_info fl">'
                content += '<div class="source fl">来源：' + news.source + '</div>'
                content += '<div class="time fl">' + news.create_time + '</div>'
                content += '</div>'
                content += '</li>'
                $(".list_con").append(content)
            }

            }else
            {

            //请求失败
            alert(resp.errmsg)
            }
    })
}
