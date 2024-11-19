const circles = document.querySelectorAll('.circle');

circles.forEach(elem =>{
    var dots = elem.getAttribute('data-dots')
     var marked = elem.getAttribute('data-percent');
     var percent = Math.floor(dots*marked/100);
     var rotate = 360/dots;
     var points = "";
    for (let index = 0; index < dots; index++) {
        points += `<div class="points" style="--i: ${index}; --rot: ${rotate}deg "></div>`;
        
    }
    elem.innerHTML = points;
    const pointsMarked = elem.querySelectorAll('.points');
    for (let index = 0; index < percent; index++) {
        pointsMarked[index].classList.add('marked')
        
    }
}
     
)

    

var ctx = document.getElementById("myChart1").getContext('2d');
    var myChart1 = new Chart(ctx, {
    type: 'pie',
    data: {
    labels:['12', '13', '1', '2', '3'],
    datasets:[{
        label: 'Orders',
        data : ['12', '13', '1', '2', '3'],
        backgroundColor: [
        'rgba(255, 99, 132, 0.9)',
        'rgba(54, 162, 235, 0.9)',
        'rgba(255, 206, 86, 0.9)',
        'rgba(75, 192, 192, 0.9)',
        'rgba(153, 23, 23, .9)' ],
        borderColor: [
        'rgba(255, 99, 132, 0.9)',
        'rgba(54, 162, 235, 0.9)',
        'rgba(255, 206, 86, 0.9)',
        'rgba(75, 192, 192, 0.9)',
        'rgba(153, 23, 23, .9)',],
        borderWidth: 1
    }]
    },
    options: {
      scales: {
        y: {  // The y-axis (ordinate)
          beginAtZero: true,
          grid: {
            display: true  // Grid lines
          }
        },
        x: {  // The x-axis (abscissa)
          grid: {
            display: true  // Grid lines
          }
        }
      }
    }})
