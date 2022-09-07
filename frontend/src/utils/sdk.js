/**
 * All trivial helper functions that could be used multiple times in different component would be placed here
 *
 */
import axios from 'axios';
import store from 'reducers/store';
import { Error } from 'config/Error';
import { notifyError, notifySuccess } from './notification';
import { BASE_BACKEND_URL } from 'constants/url';
const getBaseConfig = (method) => ({
  method,
  credentials: 'include',
  headers: { 'Content-Type': 'application/json', Authorization: `Token ${store.getState().token}` }
});

export const get = async (url, options) => {
  let response = await axios
    .get(`${BASE_BACKEND_URL}/${url}`, { ...getBaseConfig('get'), ...options })
    .catch((err) => {
      return new Error(err.message);
    });
  return response;
};

export const post = async (url, postData, options) => {
  let response = await axios
    .post(`${BASE_BACKEND_URL}/${url}`, postData, { ...getBaseConfig('post'), ...options })
    .catch((err) => {
      return new Error(err.message);
    });
  return response;
};

export const put = async (url, newData, options) => {
  let response = await axios
    .put(`${BASE_BACKEND_URL}/${url}`, newData, { ...getBaseConfig('put'), ...options })
    .catch((err) => {
      return new Error(err.message);
    });
  return response;
};

// what if really want to send data?
export const remove = async (url, removedData, options) => {
  // let response = await axios.delete(`${BASE_API_URL}/${url}`, removedData,
  let response = await axios
    .delete(`${BASE_BACKEND_URL}/${url}`, { ...getBaseConfig('delete'), ...options })
    .catch((err) => {
      return new Error(err.message);
    });
  return response;
};

export const get_url_param_last = () => {
  const url = window.location.href.split('/');
  let last_id = url.length;
  return url[last_id - 1];
};

export const get_url_param_by_id = (id, last = false) => {
  const url = window.location.href.split('/').slice(3);
  const ret = last ? url[url.length - 1] : url[id];
  return ret;
};


export const redirect = (path) => {
  window.location.href = path;
};

export const isErrorClass = (obj) => {
  return obj instanceof Error;
};
export const onSuccessOrFail = async (resp, okMsg = null, verbose = true) => {
  if (verbose) isErrorClass(resp) ? notifyError(resp.message) : notifySuccess(okMsg);

  return isErrorClass(resp) ? null : resp;
};

// ref: https://stackoverflow.com/questions/3066586/get-string-in-yyyymmdd-format-from-js-date-object

export function DisplayDetail(dateStr) {
  const d = new Date(dateStr).toString();
  return d.slice(4, 24);
}

function timeDisplayBasic(dateStr) {
  return dateStr.slice(4, 15);
}

function hourDiff(d1, d2) {
  let diffInMilliSeconds = d2 - d1;
  const millisecondPerHour = 3600 * 1000;
  let hours = Math.floor(diffInMilliSeconds / millisecondPerHour);
  return hours;
}

export function minuteDiff(d1, d2) {
  let diffInMilliSeconds = d2 - d1;
  const millisecondPerMin = 60 * 1000;
  let minutes = Math.floor(diffInMilliSeconds / millisecondPerMin);
  return minutes;
}

export function ReadEasyDate(dateStr) {
  const now = Date.now();
  const d = new Date(dateStr);
  const hd = hourDiff(d, now);
  const md = minuteDiff(d, now);
  if (md < 60) return md + 'm';
  else if (hd > 24) return timeDisplayBasic(d.toString());
  return hd + 'h';
}

export function stringEqual(str1, str2) {
  return str1.localeCompare(str2) === 0;
}
