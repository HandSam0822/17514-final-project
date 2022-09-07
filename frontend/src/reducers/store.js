import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import reducers from './reducers';

function saveToLocalStorage(state) {
  try {
    const serializedState = JSON.stringify(state);
    localStorage.setItem('state', serializedState);
  } catch (err) {
    console.log(err);
  }
}

function loadFromLocalStorage() {
  try {
    const serializedState = localStorage.getItem('state');
    if (serializedState === null) return undefined;
    return JSON.parse(serializedState);
  } catch (err) {
    console.log(err);
    return undefined;
  }
}

const persistedState = loadFromLocalStorage();
const store = createStore(reducers, persistedState, compose(applyMiddleware(thunk)));

store.subscribe(() => saveToLocalStorage(store.getState()));
export default store;

/**
 * these are what I originally write, but my state was reset everytime I rerender
 * based on what stackoverflow suggest, I should save and load redux state in localstorage
 */
// const store = createStore(reducers, compose(applyMiddleware(thunk)));
// export default store;
