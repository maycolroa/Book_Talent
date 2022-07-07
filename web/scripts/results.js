app.get('/', async (req, res) =>{

    const candidatos = await candidato.find({})
    console.log(candidatos)
    res.render('resultado')
        candidatos
})