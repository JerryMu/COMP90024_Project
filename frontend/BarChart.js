// Chart options
const options = {
  chart: {
    height: 450,
    width: "100%",
    type: "bar",
    background: "#f4f4f4",
    foreColor: "#333"
  },
  plotOptions: {
    bar: {
      horizontal: false
    }
  },
  series: [
    {
      name: "Population",
      data: [
        8550405,
        3971883,
        2720546,
        2296224,
        1567442,
        1563025,
        1469845,
        1394928,
        1300092,
        1026908
      ]
    }
  ],
  xaxis: {
    categories: [
      "New York",
      "Los Angeles",
      "Chicago",
      "Houston",
      "Philadelphia",
      "Phoenix",
      "San Antonio",
      "San Diego",
      "Dallas",
      "San Jose"
    ]
  },
  fill: {
    colors: ["#7147c9"]
  },
  dataLabels: {
    enabled: true
  },

  title: {
    text: "Largest US Cities By Population",
    align: "center",
    margin: 20,
    offsetY: 20,
    style: {
      fontSize: "16px"
    }
  }
};

// Init chart
const chart = new ApexCharts(document.querySelector("#chart"), options);

// Render chart
chart.render();

// Event example
document.getElementById("change_1").addEventListener("click", () =>
  chart.updateOptions({
    plotOptions: {
      bar: {
        horizontal: true
      }
    }
  })
);

// Event example
document.getElementById("change_2").addEventListener("click", () =>
  chart.updateOptions({
    plotOptions: {
      bar: {
        horizontal: false
      }
    }
  })
);
