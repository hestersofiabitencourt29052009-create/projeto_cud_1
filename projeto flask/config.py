

<h1 style="margin:30px ;">Usuários</h1>


<ul style="margin: 30px;">


<li>


    <a href="" style=" font-family: 'Gill Sans'; text-decoration: none;font-size: 35;background-color: aqua"> Excluir </a>
    <br>
    <a href="" style=" font-family: 'Gill Sans'; text-decoration: none;font-size: 35;background-color: aqua;"> Editar </a>


</li>



</ul>



<form action="" style="margin: 30px;">


    <input type="text">
    <button style="border-radius: 30;height: 25;width: 150;">ADD</button>




</form>
<H1 style="font-family:'Gill Sans';">EDITAR USUÁRIO</H1>


<form action="/update/{{user['id']}}">
<input name="name" value="{{users['name']}}">
<button style="border-radius: 30;height: 25;width: 150;">Salvar</button>



</form>    




<h1 style="margin:30px ;">Usuários</h1>


<ul style="margin: 30px;">
{% for u in users %}
<li>
  {{u["name"]}}
    <a href="" style=" font-family: 'Gill Sans'; text-decoration: none;font-size: 35;background-color: aqua">Excluir</a>
    <br>
    <a href="" style=" font-family: 'Gill Sans'; text-decoration: none;font-size: 35;background-color: aqua;">Editar</a>
{%endfor %}
</li>



</ul>



<form action="" style="margin: 30px;">


    <input type="text">
    <button style="border-radius: 30;height: 25;width: 150;">ADICIONAR</button>




</form>

from flask import Flask



def create_app():
    app =  Flask(
     
     __name__,
     template_folder = "../templates "


    )


    from app.controllers.user_controller import user_bp
    app.register_blueprint(user_bp)


    return app

