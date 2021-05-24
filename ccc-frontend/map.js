const dataSource = {
    chart: {
      caption: "这是我们的Welcome Page",
      subcaption: "2021",
      entityfillhovercolor: "#F8F8E9",
      numbersuffix: "Population",
      showlabels: "2",
      borderthickness: "0.4",
      theme: "fusion",
      entitytooltext:
        // "<b>$lname</b> has an average temperature of <b>$datavalue</b>"
      "Sce1： 生育率：100% 死亡率：100%\nSce2： 接种率：100% 感染率：100%\n"
  
    },
    colorrange: {
      minvalue: "231200",
      code: "#00A971",
      gradient: "1",
      color: [
        {
          minvalue: "1829375",
          maxvalue: "3658750",
          code: "#EFD951"
        }, 
        {
          minvalue: "3658750",
          maxvalue: "5488125",
          code: "#FD8963"
        },
        {
          minvalue: "5488125",
          maxvalue: "7400000",
          code: "#D60100"
        }
      ]
    },
    data: [
      {
        id: "WA",
        value: "2366900"
      },
      {
        id: "NT",
        value: "231200"
      },
      {
        id: "SA",
        value: "1659800"
      },
      {
        id: "SW",
        value: "7317500"
      },
      {
        id: "VI",
        value: "5640900"
      },
      {
        id: "TA",
        value: "511000"
      },
      {
        id: "QU",
        value: "4599400"
      }
      
    ]
  };
  
  FusionCharts.ready(function() {
    var myChart = new FusionCharts({
      type: "maps/australia",
      renderAt: "chart-container",
      width: "50%",
      height: "50%",
      dataFormat: "json",
      dataSource
    }).render();
  });