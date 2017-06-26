var a;

function increment(b){
  b = b+1;
  a = b;
}
function get_element(){
  var editor_data = CKEDITOR.instances['id_content'].getData();
  var el = document.createElement("html");
  el.innerHTML = editor_data;
  var div_arr = el.getElementsByTagName("div")
  var array = [];
  for(i=0;i<div_arr.length;i++){

    if(div_arr[i].className == "counter_id"){
      array.push(parseInt(div_arr[i].innerHTML));
    }
  }

  if(array.length<1){
    var number =0;
  }
  else{
    var number = Math.max.apply(null,array);
  }

  return number
}

CKEDITOR.dialog.add( 'accordionDialog', function ( editor ) {
    return {
        title: 'Configuração do Accordion',
        minWidth: 400,
        minHeight: 200,
        contents: [
            {
                id: 'tab-basic',
                label: 'Basic Settings',
                elements: [
                    {
                        type: 'text',
                        id: 'number',
                        label: 'Número de seções do accordion',
                        validate: CKEDITOR.dialog.validate.notEmpty( "Não pode ficar vazio" )
                    }
                ]
            }
        ],
        onOk: function() {
            a = get_element()
            increment(a);
            var dialog = this;
            var sections = parseInt(dialog.getValueOf('tab-basic','number')); //Número de seções que serão criadas
            var section =   "<div class='panel panel-default'> \
                              <div class='panel-heading'> \
                                <h4 class='panel-title'> \
                                  <a data-toggle='collapse' data-parent='#accordion' href='#a1c0'> \
                                    Collapsible Group Item \
                                  </a> \
                                </h4> \
                              </div> \
                              <div id='a1c0' class='panel-collapse collapse'> \
                                <div class='panel-body'> \
                                  Content \
                                </div> \
                              </div> \
                            </div> "
            intern = ""
            counter_html = "<div class='counter_id' style='display:none;'>".concat(a,"</div>");


              for (i=0;i<sections;i++){

                  if(i==0){
                    old_id = "a1c0";
                    old_id_href = "#a1c0";
                  }
                  else{
                    old_id = "".concat("a",a,"c",i)
                    old_id_href = "".concat("#a",a,"c",i);
                  }
                  new_id = "".concat("a",a,"c",i+1);
                  new_id_href = "".concat("#a",a,"c",i+1);

                  section = section.replace(old_id_href,new_id_href);
                  section = section.replace(old_id,new_id);

                  intern = intern + section
              }

              editor.insertHtml('<div class="panel-group" id="accordion">'+ intern + counter_html +'</div>');

        }
    };
});
