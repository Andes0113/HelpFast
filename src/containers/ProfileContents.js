import React, { useState, useEffect } from 'react';
import {
  Box, 
  HStack,
  Text
} from '@chakra-ui/react'
import axios from 'axios';

function ProfileContents() {  
  const [user, setuser] = useState({});

  var token = sessionStorage.getItem('token');
  
  useEffect(() => {
    axios.post('auth/login/', {
      id: token
    })
    .then((res) => {
      setuser(res.data.profile);
    }, (error) => {
      console.log(error);
    });
  }, []);    

  return (
    <Box as="nav" paddingTop='10vh'>
    <HStack justify={'center'} spacing='20vw' >
        { sessionStorage.getItem('token') != null ? (
          <Box>
            <Text>Welcome {user.firstName}!</Text>         
          </Box>
        ) : (
          <Box>
            <Text>Please Log In</Text>         
          </Box>
        )
        }
    </HStack>
  </Box>
    );
}

export default ProfileContents;