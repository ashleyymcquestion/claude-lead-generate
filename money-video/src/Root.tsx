import {Composition} from 'remotion';
import {MoneyIn30} from './MoneyIn30';

export const Root: React.FC = () => (
  <Composition
    id="MoneyIn30"
    component={MoneyIn30}
    durationInFrames={300}
    fps={30}
    width={1080}
    height={1920}
  />
);
