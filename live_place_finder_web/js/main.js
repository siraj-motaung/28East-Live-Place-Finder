

function DefaultMap(){
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: { 
            lat: -26.1076,
            lng: 28.0567 
        },
    });
}

document.getElementById('search-btn').addEventListener('click', async () => {
    const address = document.getElementById('address-input').value;
    const type = document.getElementById('place-type').value;

    if (!address) return alert("Please enter an address!");

});








window.onload = DefaultMap;


