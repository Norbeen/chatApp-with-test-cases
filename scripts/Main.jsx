import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Socket } from './Socket'

import { Content } from './Content';

ReactDOM.render(
    <Content />,
    document.getElementById('content')
    );
    
Socket.on('connect', function() {
    console.log('Connecting to the server!');
})
