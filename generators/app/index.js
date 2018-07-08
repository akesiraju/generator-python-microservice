var Generator = require('yeoman-generator');

module.exports = class extends Generator {
    constructor(args, opts) {
        super(args, opts);

        this.package = {
            name: 'my_python_service',
            port: 4000
        };
    }
    //Prompt user to enter application name ; default is folder name where the command is executed.
    prompting() {
        return this.prompt([{
            type: 'input',
            name: 'name',
            message: 'Your project name:',
            default: this.package.name
        }, {
            type: 'input',
            name: 'port',
            message: 'Port to run on:',
            default: 4000 // Default to port 4000
        }
        ]).then((answers) => {
            this.package.name = answers.name; // Validate this for valid folder names as supported in windows or linux
            this.package.port = answers.port || 4000;
            this.log('app name', this.package.name);
            this.log('port', this.package.port);
        });
    }

    // Copy all the files from python-service folder to the target folder and update any strings that match '<%= APP_NAME %>' with the new app name
    writing() {
        this.fs.copyTpl(this.templatePath('python_service'), this.destinationPath(this.package.name), { APP_NAME: this.package.name, PORT: this.package.port });
    }
}
