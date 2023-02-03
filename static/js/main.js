window.onload = () => {
    let loader = document.querySelector("#preloader");
    // loader.style.opacity = 0;
    //  loader.style.visibility = "hidden";
    setTimeout(() => {
      loader.style.opacity = 0;
     loader.style.visibility = "hidden";
    }, 500)
  };


  function searchResults(data){
    let result_search = document.querySelector('.result_search').style.display = 'block'
    let ul_search = document.querySelector('.ul_search');
    let results;
    ul_search.innerHTML = ''
    if (data.length==0) {
      ul_search.innerHTML=`
      <li class="text-center color border py-5 d-flex justify-content-center align-items-center flex-column">
            <h2>Ma'lumot topilmadi</h2>
            <lottie-player
                src="https://assets10.lottiefiles.com/packages/lf20_dmw3t0vg.json"
                speed="1"
                style="width: 200px; height: 200px"
                loop
                autoplay
            ></lottie-player>
        </li>
      `
    }
    else{
      data.forEach((item) => {
        let url = 'article_detail/' + item.fields.slug
        let li_item = `<li class="border py-2"><a href="${url}">${item.fields.name}</a></li>`
        if (!ul_search.innerHTML.match(li_item)) {
          ul_search.innerHTML += li_item
        }
      });
    }
  }

function dark() {
  let dark_light = document.querySelector('.dark_light').childNodes[1];
  const body_tag =  document.body
  let theme;

  if (dark_light.classList.contains('fa-moon')) {
    dark_light.classList.add('fa-sun')
    dark_light.classList.remove('fa-moon')
    theme = 'true'
    body_tag.classList.add('dark')
  } else{
    dark_light.classList.remove('fa-sun')
    dark_light.classList.add('fa-moon')
    theme = 'false'
    body_tag.classList.remove('dark')
  }
  localStorage.setItem('dark', theme);
  
}


let bodyTheme = localStorage.getItem("dark")
if (bodyTheme == 'true') {
  dark()
}