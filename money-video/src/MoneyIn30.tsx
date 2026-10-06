import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

const GOLD = 'linear-gradient(180deg, #fff1b8 0%, #f5c542 45%, #b8860b 100%)';

export const MoneyIn30: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();

  const scale = spring({frame, fps, config: {damping: 12}});
  const fadeIn = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: 'clamp'});
  const fadeOut = interpolate(frame, [durationInFrames - 20, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp',
  });
  const glow = 20 + 15 * Math.sin(frame / 10);

  return (
    <AbsoluteFill style={{backgroundColor: '#000', justifyContent: 'center', alignItems: 'center'}}>
      <div
        style={{
          fontFamily: 'Georgia, "Times New Roman", serif',
          fontWeight: 900,
          fontSize: 230,
          lineHeight: 1.05,
          textAlign: 'center',
          background: GOLD,
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          filter: `drop-shadow(0 0 ${glow}px rgba(245,197,66,0.6))`,
          opacity: fadeIn * fadeOut,
          transform: `scale(${0.6 + 0.4 * scale})`,
        }}
      >
        Money
        <br />
        in 30
      </div>
    </AbsoluteFill>
  );
};
