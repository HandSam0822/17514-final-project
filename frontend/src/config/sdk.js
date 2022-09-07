import { minuteDiff } from 'utils/sdk';
export const tokenExpire = (lastLogin, expireTime) => {
  const d = new Date(lastLogin);
  const now = Date.now();
  console.log(d);
  console.log(now);
  const md = minuteDiff(d, now);
  console.log(md);
  return md > expireTime;
};
