import React from 'react';
import {
  Box, 
  HStack,
  Text
} from '@chakra-ui/react'

function ProfileContents() {  
  return (
    <Box as="nav" paddingTop='10vh'>
    <HStack justify={'center'} spacing='20vw' >
      <Text>Write Profile Contents Here</Text>
    </HStack>
  </Box>
    );
}

export default ProfileContents;