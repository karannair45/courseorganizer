function addRow () {
    var myTable = document.getElementById("schedule");
    var currentIndex = myTable.rows.length;
    var currentRow = myTable.insertRow(-1);

    var dateBox = document.createElement("input");
    dateBox.setAttribute("name", "schedule[date]" + currentIndex);

    var topicBox = document.createElement("input");
    topicBox.setAttribute("name", "schedule[topic]" + currentIndex);

    var assignmentBox = document.createElement("input");
    assignmentBox.setAttribute("name", "schedule[assignment]" + currentIndex);
    
    var labBox = document.createElement("input");
    labBox.setAttribute("name", "schedule[lab]" + currentIndex);
    
    var discussionBox = document.createElement("input");
    discussionBox.setAttribute("name", "schedule[discussion]" + currentIndex);

    var quizBox = document.createElement("input");
    quizBox.setAttribute("name", "schedule[quiz]" + currentIndex);

    var examBox = document.createElement("input");
    examBox.setAttribute("name", "schedule[exam" + currentIndex);

    var currentCell = currentRow.insertCell(-1);
    currentCell.appendChild(dateBox);

    currentCell = currentRow.insertCell(-1);
    currentCell.appendChild(topicBox);

    currentCell = currentRow.insertCell(-1);
    currentCell.appendChild(assignmentBox);

    currentCell = currentRow.insertCell(-1);
    currentCell.appendChild(labBox);

    currentCell = currentRow.insertCell(-1);
    currentCell.appendChild(discussionBox);

    currentCell = currentRow.insertCell(-1);
    currentCell.appendChild(quizBox);

    currentCell = currentRow.insertCell(-1);
    currentCell.appendChild(examBox);
}

function removeRow() {
    document.getElementById("schedule").deleteRow(-1);
}