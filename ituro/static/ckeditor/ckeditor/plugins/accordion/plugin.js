CKEDITOR.plugins.add( 'accordion', {
    icons: 'accordion',
    init: function( editor ) {
        //adicionando o comando
        editor.addCommand( 'accordionDialog', new CKEDITOR.dialogCommand( 'accordionDialog' ) );

        //setando o botão
        editor.ui.addButton('Accordion', {
            label: 'Insert Accordion',
            command: 'accordionDialog',
            toolbar: 'insert'
        });

        //Adicionando a janela de dialogo
        CKEDITOR.dialog.add( 'accordionDialog', this.path + 'dialogs/accordion.js' );


    }
});
