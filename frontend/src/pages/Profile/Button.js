import React from 'react'
import { redirect } from 'utils/sdk'
import { Button } from 'react-bootstrap'
export const EditButton = () => {
  return (
    <Button variant="primary" onClick={() => redirect('/settings/profile')}>Edit profile</Button>
  )
}

export const FollowUnfollowButton = (props) => {
  return (
    <Button variant="primary" 
    onClick={() => props.onClick()}>
    {props.following ? 'Unfollow' : 'Follow'}
    </Button>
  )
}

