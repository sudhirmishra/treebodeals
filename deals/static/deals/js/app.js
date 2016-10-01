var nextUrl;
var prevUrl;
var base_url = ":8000/deals/?format=json"
var stats_url = ":8000/stat/"

jQuery(document).ready(function() {
    
    base_url = "http://"+window.location.hostname + base_url

    fetchData(base_url);
    fetchStats();
    jQuery('#pagePrev').click(function(){
        if(prevUrl != null){
            clear_div()
            fetchData(prevUrl);    
        }        
    });   
    
    jQuery('#pageNext').click(function(){
        if(nextUrl != null){
            clear_div()
            fetchData(nextUrl);    
        }        
    });   
    
});

function fetchData(url){
    jQuery.getJSON( url ,function (data) {
        console.log(data);
        nextUrl = data.next;
        prevUrl = data.previous;
        var directive = {
            'div':{
                'deal<-results':{ 
                    'h4': 'deal.name',
                    'p':'deal.location',
                    'a.btn@href':'deal.link',
                    '.card-img-top@src':'deal.image'
                    }
            }
        };
        $p( '#data' ).render( data, directive );
    }); 
}
function fetchStats(){
    var url = "http://"+window.location.hostname + stats_url;
    jQuery.getJSON( url ,function (data) {
        console.log(data);
        jQuery("#avg").html(data['average_rating']);
        jQuery("#maxmin").html(data['price']['maximum'] + " / " + data['price']['minimum']);
        
        jQuery("#area").html(data['area-wise-hotel-distribution']);
        
        var directive = {
            'span':{
                'city<-area-wise-hotel-distribution':{ 
                    'span.city': 'city[0]',
                    'span.count':'city[1]',
                    }
            }
        };
        $p( '#area' ).render( data, directive );
        
    
});
     
}
function clear_div(){
    html = '<div class="col-lg-4"><div class="card"><div class="card-block"><img class="card-img-top" src="#" alt="Card image cap"><h4 class="card-title">Card title</h4><p class="card-text"></p><a class="btn btn-primary">More Details</a></div></div></div>';
    
    jQuery("#data").html(html);

}