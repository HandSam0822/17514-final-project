import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { toastBaseConfig } from './config';
import { devil_emoji, bless_emoji } from './emoji';

// if not configure, toast won't show
toast.configure();
export const notifyError = (error, options) => {
  if (error) error = devil_emoji + '  ' + error;
  else error = devil_emoji + ' Something went wrong.';

  options = options || toastBaseConfig;
  console.log(error);
  toast.error(error, options);
};

export const notifySuccess = (msg, options) => {
  msg = bless_emoji + '  ' + msg || bless_emoji + ' Success operation';
  options = options || toastBaseConfig;
  toast.success(msg, options);
};
