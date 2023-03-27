const table = document.getElementById("schedule");
const radioNo = document.getElementById("check16");

function addRow() {
    var date = document.getElementById("date").value;
    var topic = document.getElementById("topic").value;
    var assignment = document.getElementById("assignment").value;
    var lab = document.getElementById("lab").value;
    var discussion = document.getElementById("discussion").value;
    var quiz = document.getElementById("quiz").value;
    var exam = document.getElementById("exam").value;

    var table = document.getElementById("schedule");
    var row = table.insertRow(-1);

    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);
    var cell7 = row.insertCell(6);

    cell1.innerHTML = date;
    cell2.innerHTML = topic;
    cell3.innerHTML = assignment;
    cell4.innerHTML = lab;
    cell5.innerHTML = discussion;
    cell6.innerHTML = quiz;
    cell7.innerHTML = exam;
  }

function removeRow() {
    document.getElementById("schedule").deleteRow(-1);
}

radioNo.addEventListener("click", () => {
  const columnIndexToRemove = 6;

  for (let i = 0; i < table.rows.length; i++) {
    table.rows[i].deleteCell(columnIndexToRemove);
  }
});
