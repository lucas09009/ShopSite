function Search_byNAME(){
    let saisie
    saisie = document.getElementById("Search").value
    lien = '/product/search/by-name/'+saisie
    window.location.href = lien
}

function Search_by_category(){
    let saisie = document.getElementById("Search").value.split(" ").join("")
    lien = '/search/by-category/'+saisie
    window.location.href = lien
}

function Search_byID(){
    let saisie
    saisie = document.getElementById("Search").value.split(" ").join("")
    lien = '/product/'+saisie
    window.location.href = lien
}

function More_details(product_id){
    window.location.href = '/product/'+ product_id
}

