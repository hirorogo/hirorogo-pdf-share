fetch("/list-books")
  .then(response => response.json())
  .then(files => {
    document.getElementById("searchBox").addEventListener("input", function() {
      let query = this.value.toLowerCase();
      let results = files.filter(file => file.toLowerCase().includes(query));
      let resultList = document.getElementById("resultList");
      resultList.innerHTML = "";
      results.forEach(file => {
        let li = document.createElement("li");
        li.innerHTML = `<a href="/pdfjs/web/viewer.html?file=/books/${file}">${file}</a>`;
        resultList.appendChild(li);
      });
    });
  });
