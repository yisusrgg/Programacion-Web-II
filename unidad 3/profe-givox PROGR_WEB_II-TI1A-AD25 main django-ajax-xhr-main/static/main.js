// https://docs.djangoproject.com/en/3.2/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function getAllTodos(url) {
  (async () => {
    try {
      const response = await fetch(url, {
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        }
      });
      const data = await response.json();

      const todoList = document.getElementById("todoList");
      todoList.innerHTML = "";

      (data.context).forEach(todo => {
        const todoHTMLElement = `
          <li>
            <p>Task: ${todo.task}</p>
            <p>Completed?: ${todo.completed}</p>
          </li>`
        todoList.innerHTML += todoHTMLElement;
      });
    } catch (err) {
      console.error('Error fetching todos:', err);
    }
  })();
}



const operationGetAllTodos = async (url) => {
  try {
    const r = await fetch(url, {
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      }
    });
    const dt = await r.json();

    const todoList = document.getElementById("todoList");
    todoList.innerHTML = "";

    (dt.context).forEach(todo => {
      const todoHTMLElement = `
        <li>
          <p>Task: ${todo.task}</p>
          <p>Completed?: ${todo.completed}</p>
        </li>`
      todoList.innerHTML += todoHTMLElement;
    });
  } catch (err) {
    console.error('Error in operationGetAllTodos:', err);
  }

};


async function addTodo(url, payload) {
  try {
    const response = await fetch(url, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({payload: payload})
    });

    const data = await response.json();
    console.log(data);
    return data;
  } catch (err) {
    console.error('Error adding todo:', err);
    throw err;
  }
}


async function updateTodo(url, payload) {
  try {
    const response = await fetch(url, {
      method: "PUT",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({payload: payload})
    });

    const data = await response.json();
    console.log(data);
    return data;
  } catch (err) {
    console.error('Error updating todo:', err);
    throw err;
  }
}


async function deleteTodo(url) {
  try {
    const response = await fetch(url, {
      method: "DELETE",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
      }
    });

    const data = await response.json();
    console.log(data);
    return data;
  } catch (err) {
    console.error('Error deleting todo:', err);
    throw err;
  }
}
