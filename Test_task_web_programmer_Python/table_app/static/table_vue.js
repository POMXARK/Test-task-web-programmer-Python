new Vue({
    el: '#table_vue',
    data: {
        table_rows:[]
    },
    created: function(){
        const vm = this;
        axios.get('')
        .then(function (response){
            console.log(response.data)
        })
    }
}

)