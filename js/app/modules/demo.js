import {demo_af} from "./a.js";
demo_af();

import {b as b_alias} from './b.js';
b_alias.demo_bf();

import d_alias from './d.js';
d_alias();

import E_alias from './e.js';
let ee = new E_alias();
ee.demo_ef();

import ff from './f.js';
ff.demo_ff();

// See g.js for a best way how to organise a module
import g_alias from './g.js';
g_alias.demo_gf();
