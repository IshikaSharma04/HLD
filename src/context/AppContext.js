
// Logged: 2026-05-08 09:15:00
import React, { createContext, useReducer } from 'react';
export const AppContext = createContext();
export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer((s, a) => s, {});
  return <AppContext.Provider value={{ state, dispatch }}>{children}</AppContext.Provider>;
};

// Logged: 2026-05-09 15:20:00
import React, { createContext, useReducer } from 'react';
export const AppContext = createContext();
export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer((s, a) => s, {});
  return <AppContext.Provider value={{ state, dispatch }}>{children}</AppContext.Provider>;
};
