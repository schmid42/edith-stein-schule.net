const path = require('path');


const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const RemovePlugin = require('remove-files-webpack-plugin');
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
    // https://stackoverflow.com/questions/35903246/how-to-create-multiple-output-paths-in-webpack-config
    entry: {
        'main/static/bundle_main': './main/js/main.js',
        'home/static/bundle_home': './home/js/main.js',
        'blog/static/bundle_blog': './blog/js/main.js',
        'content/static/bundle_content': './content/js/main.js',
        'photowall/static/bundle_photowall': './photowall/js/main.js',
    },
    output: {
        path: path.resolve(__dirname, '../backend'),
        filename: '[name].js',
    },
    devtool: "eval-cheap-source-map",
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: 'asset/resource',
                generator: {
                    filename: 'main/static/fonts/[name][ext]'
                }
            },
        ]
    },
    plugins: [
        new RemovePlugin({
            before: {
                root: '../backend',
                include: [
                    'main/static',
                    'main/templates',
                    'home/static',
                    'home/templates',
                    'content/static',
                    'content/templates',
                    'blog/static',
                    'blog/templates',
                    'photowall/static',
                    'photowall/templates',
                    'search/templates'
                ],
                log: true,
                recursive: true
            },
            watch: {
                // parameters for "before watch compilation" stage.
            },
            after: {
                // parameters for "after normal and watch compilation" stage.
            }
        }),
        new CopyPlugin({
            patterns: [
                { from: './main/templates', to: '../backend/main/templates', force: true },
                { from: './home/templates', to: '../backend/home/templates', force: true },
                { from: './content/templates', to: '../backend/content/templates', force: true },
                { from: './blog/templates', to: '../backend/blog/templates', force: true },
                { from: './photowall/templates', to: '../backend/photowall/templates', force: true },
                { from: './search/templates', to: '../backend/search/templates', force: true },
                {
                    from: './assets', to: '../backend/main/static/assets', force: true,
                    globOptions: {
                        ignore: [
                            // Ignore all subdirectories called 'src'
                            "**/src"
                        ],
                    }
                },
                { from: './node_modules/ionicons/dist/ionicons', to: '../backend/main/static/ionicons/ionicons', force: true }
            ],
            options: {}
        }),
        new MiniCssExtractPlugin({
            filename: '[name].css'
        })
    ]
};

